# Auth Service Design Specification

> **Owner:** Identity Team | **Version:** 2.3 | **Last Updated:** 2026-03-05

## Responsibilities

The Auth Service owns all identity and access management for the platform:

- User authentication (email/password, SSO via SAML/OIDC, magic link)
- Token issuance and validation (JWT, refresh tokens)
- Organization and team management
- Role-based access control (RBAC) — role assignment and permission checks
- API key lifecycle management
- Multi-factor authentication (TOTP, WebAuthn)
- Session management

## Service Boundaries

The Auth Service **does not** own:
- Authorization logic for specific resources (e.g., "can user X view workflow Y") — this is enforced by each resource service using the roles/scopes provided in the JWT
- User preferences or profile data beyond identity fields
- Audit logging (it emits events; the audit service consumes them)

---

## API Reference

### Token Endpoints

```
POST /auth/token          — Username/password login, returns JWT + refresh token
POST /auth/refresh        — Exchange refresh token for new JWT
POST /auth/revoke         — Revoke a refresh token
POST /auth/token/sso      — Exchange SAML assertion or OIDC code for JWT
POST /auth/token/magic    — Exchange magic link token for JWT
GET  /.well-known/jwks.json — Public key set for JWT verification
```

### Management Endpoints (require admin role)

```
GET|POST   /auth/users              — List/create users
GET|PUT    /auth/users/:id          — Get/update user
DELETE     /auth/users/:id          — Deactivate user (soft delete)
POST       /auth/users/:id/mfa      — Enroll MFA
GET|POST   /auth/orgs               — List/create organizations
GET|PUT    /auth/orgs/:id           — Get/update org
POST       /auth/orgs/:id/members   — Add org member
DELETE     /auth/orgs/:id/members/:userId — Remove member
GET|POST   /auth/api-keys           — List/create API keys
DELETE     /auth/api-keys/:id       — Revoke API key
```

---

## Data Model

```sql
-- Core identity tables
organizations (id, name, slug, plan_tier, sso_config, created_at)
users (id, org_id, email, password_hash, mfa_secret, status, created_at)
sessions (id, user_id, refresh_token_hash, expires_at, ip, user_agent)
api_keys (id, user_id, org_id, name, key_hash, scopes[], last_used_at, expires_at)

-- Access control
roles (id, org_id, name, permissions[])
user_roles (user_id, role_id, granted_at, granted_by)
teams (id, org_id, name)
team_memberships (team_id, user_id, role)
```

---

## JWT Structure

```json
{
  "sub": "usr_01hx4k2m3n5p6q7r8s9t0",
  "iss": "https://auth.apei-platform.com",
  "aud": "https://api.apei-platform.com",
  "exp": 1711234567,
  "iat": 1711230967,
  "org": "org_01hx4k2m3n5p6q7r8s9t0",
  "roles": ["member", "workflow:admin"],
  "scopes": ["workflows:read", "workflows:write", "executions:read"],
  "plan": "enterprise",
  "jti": "tok_01hx4k2m3n5p6q7r8s9t0"
}
```

Token lifetime: **15 minutes** (short-lived to minimize exposure window)
Refresh token lifetime: **30 days** (rotated on each use — refresh token rotation)

---

## Security Design

| Concern | Implementation |
|---------|---------------|
| Password storage | bcrypt, cost factor 12 |
| Token signing | RS256 (2048-bit RSA); private key in Vault Transit engine |
| Refresh token storage | SHA-256 hash stored; plaintext never persisted |
| Rate limiting | 5 failed logins → 15-min lockout; 20 req/min per IP on auth endpoints |
| MFA | TOTP (RFC 6238) + WebAuthn (FIDO2 passkeys) |
| SSO | SAML 2.0 + OIDC/OAuth 2.0; IdP metadata validated on configuration |
| Session fixation | New session ID issued on every authentication event |

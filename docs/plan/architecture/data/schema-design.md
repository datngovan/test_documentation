# Database Schema Design

> **Owner:** Data Team | **Last Updated:** 2026-03-08

## Design Principles

1. **UUIDs v7** everywhere — time-ordered, globally unique, no sequential ID exposure
2. **Soft deletes** — `deleted_at TIMESTAMPTZ` instead of physical deletion; data is retained for audit
3. **Immutable versions** — workflow definitions are versioned and never updated in-place
4. **Tenant isolation** — every table has `org_id`; row-level security policies enforce it
5. **Audit trail** — all mutations emit change events via Postgres logical replication → audit schema

---

## Core Schema

### `workflows` table

```sql
CREATE TABLE workflows (
    id              UUID PRIMARY KEY DEFAULT gen_ulid(),
    org_id          UUID NOT NULL REFERENCES organizations(id),
    name            TEXT NOT NULL,
    slug            TEXT NOT NULL,
    description     TEXT,
    status          TEXT NOT NULL DEFAULT 'draft'
                    CHECK (status IN ('draft', 'active', 'paused', 'archived')),
    current_version INTEGER NOT NULL DEFAULT 1,
    tags            TEXT[] DEFAULT '{}',
    created_by      UUID NOT NULL REFERENCES users(id),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    deleted_at      TIMESTAMPTZ,

    CONSTRAINT workflows_org_slug_unique UNIQUE (org_id, slug)
);

-- Indexes
CREATE INDEX idx_workflows_org_status ON workflows (org_id, status) WHERE deleted_at IS NULL;
CREATE INDEX idx_workflows_org_updated ON workflows (org_id, updated_at DESC) WHERE deleted_at IS NULL;
CREATE INDEX idx_workflows_tags ON workflows USING GIN (tags);
```

### `workflow_versions` table (immutable)

```sql
CREATE TABLE workflow_versions (
    id              UUID PRIMARY KEY DEFAULT gen_ulid(),
    workflow_id     UUID NOT NULL REFERENCES workflows(id),
    org_id          UUID NOT NULL REFERENCES organizations(id),
    version         INTEGER NOT NULL,
    definition      JSONB NOT NULL,   -- full workflow DAG as JSON
    checksum        TEXT NOT NULL,    -- SHA-256 of definition for integrity
    created_by      UUID NOT NULL REFERENCES users(id),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    -- No updated_at — versions are immutable
    -- No deleted_at — versions are never deleted

    CONSTRAINT wf_versions_unique UNIQUE (workflow_id, version)
);
```

### `executions` table

```sql
CREATE TABLE executions (
    id              UUID PRIMARY KEY DEFAULT gen_ulid(),
    workflow_id     UUID NOT NULL REFERENCES workflows(id),
    workflow_version INTEGER NOT NULL,
    org_id          UUID NOT NULL REFERENCES organizations(id),
    status          TEXT NOT NULL DEFAULT 'pending'
                    CHECK (status IN ('pending','running','succeeded','failed','cancelled','timed_out')),
    trigger_type    TEXT NOT NULL CHECK (trigger_type IN ('manual','schedule','webhook','api','sub_workflow')),
    trigger_payload JSONB,
    context         JSONB,            -- runtime context (secrets resolved, params bound)
    output          JSONB,            -- final output after execution
    error           JSONB,            -- error details if failed
    started_at      TIMESTAMPTZ,
    completed_at    TIMESTAMPTZ,
    duration_ms     INTEGER GENERATED ALWAYS AS (
                        EXTRACT(EPOCH FROM (completed_at - started_at)) * 1000
                    ) STORED,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Partitioned by month for performance
-- Partition example:
CREATE TABLE executions_2026_03 PARTITION OF executions
    FOR VALUES FROM ('2026-03-01') TO ('2026-04-01');

-- Indexes (on each partition via inheritance)
CREATE INDEX idx_executions_org_workflow ON executions (org_id, workflow_id, started_at DESC);
CREATE INDEX idx_executions_status ON executions (org_id, status) WHERE status IN ('pending','running');
```

---

## Query Patterns & Performance Notes

### Frequently executed queries

| Query | Execution plan target | Index used |
|-------|----------------------|-----------|
| List workflows for org (paginated) | Index scan + limit | `idx_workflows_org_updated` |
| Get execution history for workflow | Index scan + partition pruning | `idx_executions_org_workflow` |
| Count running executions per org | Index-only scan | `idx_executions_status` |
| Full-text search across workflow names | Index scan | GIN on `to_tsvector(name)` |
| Find workflows with a specific tag | Bitmap index scan | `idx_workflows_tags` (GIN) |

### Connection pooling

All services connect via **PgBouncer** in transaction mode:
- Max pool size per service: 20 connections
- Server pool size (PgBouncer → Postgres): 100
- Statement timeout: 30 seconds
- Idle connection timeout: 300 seconds
- Applications must use short transactions; no long-running interactive sessions

---

## Migration Policy

- All schema changes via Flyway migrations in `db/migrations/`
- Naming: `V{timestamp}__{description}.sql` (e.g., `V20260310143000__add_execution_duration_column.sql`)
- Zero-downtime migrations required for all production changes:
  - Add nullable columns — OK anytime
  - Add NOT NULL columns — add nullable first, backfill, add constraint in separate migration
  - Drop columns — mark deprecated in code first, remove usages, then drop in next release
  - Rename columns — use a view or two-phase approach (add new, dual-write, migrate reads, drop old)
- Migration rollback plan documented in migration comment header for any destructive change

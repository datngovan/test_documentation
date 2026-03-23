# Integration Testing Guide

> **Owner:** Engineering Quality Guild | **Last Updated:** 2026-03-01

## What Integration Tests Cover

Integration tests verify that **multiple components work together correctly** — service + database, service + queue, or service + downstream API. They use real infrastructure (usually in Docker via `testcontainers-go`) and run in CI but not during local development hot-reload.

Integration tests live in `./tests/integration/` and are separated from unit tests by build tag:

```go
//go:build integration
```

Run them with:
```bash
go test ./tests/integration/... -tags integration -v -timeout 10m
```

---

## Test Environment Setup

### Using `testcontainers-go`

```go
package integration_test

import (
    "context"
    "testing"

    "github.com/testcontainers/testcontainers-go"
    "github.com/testcontainers/testcontainers-go/modules/postgres"
    "github.com/testcontainers/testcontainers-go/modules/kafka"
)

func setupTestEnvironment(t *testing.T) (pgDSN string, kafkaBroker string, teardown func()) {
    ctx := context.Background()

    // Start Postgres
    pgContainer, err := postgres.RunContainer(ctx,
        testcontainers.WithImage("postgres:16-alpine"),
        postgres.WithDatabase("apei_test"),
        postgres.WithUsername("test"),
        postgres.WithPassword("test"),
    )
    require.NoError(t, err)

    pgDSN, err = pgContainer.ConnectionString(ctx, "sslmode=disable")
    require.NoError(t, err)

    // Run migrations
    err = runMigrations(pgDSN)
    require.NoError(t, err)

    // Start Kafka
    kafkaContainer, err := kafka.RunContainer(ctx,
        testcontainers.WithImage("confluentinc/cp-kafka:7.6.0"),
    )
    require.NoError(t, err)

    kafkaBroker, err = kafkaContainer.Brokers(ctx)
    require.NoError(t, err)

    teardown = func() {
        pgContainer.Terminate(ctx)
        kafkaContainer.Terminate(ctx)
    }
    return
}
```

---

## Test Scope Matrix

| Test Name | Services Involved | Infrastructure | Run Time |
|-----------|------------------|---------------|---------|
| `WorkflowCRUD_Test` | workflow-engine + PostgreSQL | PostgreSQL | ~3s |
| `WorkflowExecution_HappyPath` | workflow-engine + orchestrator + Kafka | PostgreSQL, Kafka | ~8s |
| `StepHandler_HTTPRequest` | step handler + mock HTTP server | None (mock) | ~1s |
| `StepHandler_DatabaseInsert` | step handler + PostgreSQL | PostgreSQL | ~4s |
| `AuthService_LoginFlow` | auth-service + PostgreSQL | PostgreSQL | ~2s |
| `AuthService_SSOFlow` | auth-service + mock IdP + PostgreSQL | PostgreSQL | ~3s |
| `SchedulerService_CronTrigger` | scheduler + Kafka + workflow-engine | PostgreSQL, Kafka | ~12s |

Total CI run time target: **< 8 minutes**

---

## Data Management

### Fixture Strategy

Each test creates its own isolated data using the `TestFixtures` helper:

```go
func TestWorkflowExecution_RetriesOnTransientFailure(t *testing.T) {
    ctx := context.Background()
    pgDSN, kafkaBroker, teardown := setupTestEnvironment(t)
    defer teardown()

    // Create isolated test org and user
    fixtures := NewTestFixtures(pgDSN)
    org := fixtures.CreateOrg(t, "test-org")
    user := fixtures.CreateUser(t, org.ID, "test@example.com")
    token := fixtures.CreateToken(t, user.ID)

    // Define a workflow that fails transiently
    workflowDef := WorkflowDefinition{
        Name: "retry-test-workflow",
        Steps: []Step{
            {
                ID:   "flaky-step",
                Type: "http_request",
                Config: map[string]any{
                    "url":    mockServer.URL + "/flaky-endpoint",  // returns 503 twice, then 200
                    "method": "GET",
                },
                ErrorHandler: ErrorHandler{
                    Type:       "retry",
                    MaxRetries: 3,
                    Backoff:    "exponential",
                    InitialDelay: "100ms",
                },
            },
        },
    }

    // Execute and verify retry behavior
    executionID := triggerWorkflow(t, token, workflowDef)
    execution := waitForCompletion(t, token, executionID, 30*time.Second)

    assert.Equal(t, "succeeded", execution.Status)
    assert.Equal(t, 3, execution.Steps["flaky-step"].AttemptCount)
    assert.Equal(t, "succeeded", execution.Steps["flaky-step"].Status)
}
```

### Cleanup Policy

- Each test creates data under a unique `org_id` — no cross-test pollution
- `defer teardown()` destroys the entire container (including all data) after each test suite
- Never truncate tables in a shared database — always use isolated containers

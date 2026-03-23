# Unit Testing Guide

> **Owner:** Engineering Quality Guild | **Last Updated:** 2026-03-01

## Philosophy

A unit test verifies a single piece of logic in complete isolation — no network, no database, no filesystem. If your test calls `time.Sleep`, reads from a port, or writes to a file, it is not a unit test.

**Why this matters:** Unit tests should run in < 30 seconds total. If they take longer, engineers stop running them locally, and CI becomes the first place bugs are caught — which is too late.

---

## What to Test

| Category | Test? | Why |
|----------|-------|-----|
| Business logic (parsing, validation, transformation) | ✅ Always | Core value, pure functions, easy to test |
| Error handling and edge cases | ✅ Always | Common source of production bugs |
| Data mapping between layers | ✅ Always | Silent corruption bugs are hard to detect otherwise |
| Public API of a module | ✅ Always | Interface contract |
| Private implementation details | ❌ No | Couples tests to implementation, makes refactoring painful |
| Database queries | ❌ No | Integration test territory |
| HTTP handlers | ⚠️ Sparingly | Test request parsing and response serialization; not the business logic inside |
| Happy path only | ❌ Never | Error paths have more bugs than happy paths |

---

## Test Structure — Arrange / Act / Assert

Every test follows the AAA pattern with a blank line between each section:

```go
func TestWorkflowParser_ValidatesStepDependencies(t *testing.T) {
    // Arrange
    definition := WorkflowDefinition{
        Steps: []Step{
            {ID: "step-a", Type: "http_request"},
            {ID: "step-b", Type: "jq_transform", DependsOn: []string{"step-a"}},
            {ID: "step-c", Type: "jq_transform", DependsOn: []string{"step-b", "step-a"}},
        },
    }
    parser := NewWorkflowParser(defaultConfig())

    // Act
    graph, err := parser.Parse(definition)

    // Assert
    require.NoError(t, err)
    assert.Len(t, graph.Nodes, 3)
    assert.Equal(t, []string{"step-a"}, graph.Dependencies("step-b"))
    assert.ElementsMatch(t, []string{"step-b", "step-a"}, graph.Dependencies("step-c"))
}
```

---

## Table-Driven Tests

For functions with multiple input → output cases, always use table-driven tests:

```go
func TestStepHandlerRegistry_Lookup(t *testing.T) {
    registry := NewStepHandlerRegistry()
    registry.Register("http_request", &HTTPRequestHandler{})
    registry.Register("jq_transform", &JQTransformHandler{})

    tests := []struct {
        name        string
        stepType    string
        expectFound bool
        expectType  string
    }{
        {
            name:        "registered handler is found",
            stepType:    "http_request",
            expectFound: true,
            expectType:  "*handlers.HTTPRequestHandler",
        },
        {
            name:        "registered transform handler found",
            stepType:    "jq_transform",
            expectFound: true,
            expectType:  "*handlers.JQTransformHandler",
        },
        {
            name:        "unknown handler returns not found",
            stepType:    "does_not_exist",
            expectFound: false,
        },
        {
            name:        "empty step type returns not found",
            stepType:    "",
            expectFound: false,
        },
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            handler, found := registry.Lookup(tt.stepType)
            assert.Equal(t, tt.expectFound, found)
            if tt.expectFound {
                assert.Equal(t, tt.expectType, fmt.Sprintf("%T", handler))
            }
        })
    }
}
```

---

## Coverage Requirements

| Package | Minimum Coverage | Rationale |
|---------|-----------------|-----------|
| `engine/parser` | 90% | Critical correctness — parsing errors corrupt all downstream execution |
| `engine/executor` | 85% | Complex branching logic, many failure modes |
| `engine/handlers/*` | 80% | Each handler is independently testable and customer-facing |
| `api/middleware` | 80% | Security-critical code |
| `api/handlers` | 70% | HTTP plumbing; integration tests cover this better |
| `pkg/util/*` | 75% | Shared utilities, many callers |

Coverage is enforced in CI — PRs failing the coverage threshold will not merge.

```bash
# Check coverage locally
go test ./... -coverprofile=coverage.out
go tool cover -func=coverage.out | tail -1
# Must show: total: (statements) XX.X%
```

---

## Common Anti-Patterns to Avoid

| Anti-pattern | Problem | Fix |
|-------------|---------|-----|
| `time.Sleep` in tests | Makes tests slow and flaky | Use `clock.Mock` or channel synchronization |
| Testing private functions directly | Couples to implementation | Test via public API; if private logic is complex enough to test directly, extract it |
| Asserting on exact error message strings | Fragile — messages change | Use `errors.Is()` or check error type |
| One test that covers multiple behaviors | Hard to debug on failure | One test per behavior (table-driven is fine) |
| Shared mutable state between tests | Order-dependent, flaky | Each test creates its own fixtures |
| `fmt.Println` debugging left in test | Noisy CI output | Use `t.Logf` which only prints on failure |

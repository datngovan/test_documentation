# Hướng Dẫn Kiểm Thử Đơn Vị

> **Chủ sở hữu:** Engineering Quality Guild | **Cập nhật lần cuối:** 2026-03-01

## Triết Lý

Kiểm thử đơn vị xác minh một phần logic duy nhất trong sự cách ly hoàn toàn — không mạng, không cơ sở dữ liệu, không hệ thống tập tin. Nếu kiểm thử của bạn gọi `time.Sleep`, đọc từ một cổng, hoặc ghi vào tập tin, đó không phải kiểm thử đơn vị.

**Tại sao điều này quan trọng:** Kiểm thử đơn vị nên chạy trong vòng 30 giây. Nếu mất lâu hơn, kỹ sư ngừng chạy chúng cục bộ, và CI trở thành nơi đầu tiên phát hiện lỗi — điều đó là quá muộn.

---

## Nên Kiểm Thử Gì

| Danh mục | Kiểm thử? | Tại sao |
|---------|----------|---------|
| Logic kinh doanh (phân tích, xác thực, chuyển đổi) | ✅ Luôn luôn | Giá trị cốt lõi, hàm thuần, dễ kiểm thử |
| Xử lý lỗi và trường hợp biên | ✅ Luôn luôn | Nguồn phổ biến của lỗi production |
| Ánh xạ dữ liệu giữa các lớp | ✅ Luôn luôn | Lỗi hỏng dữ liệu âm thầm khó phát hiện |
| API công khai của module | ✅ Luôn luôn | Hợp đồng giao diện |
| Chi tiết triển khai nội bộ | ❌ Không | Gắn chặt kiểm thử với triển khai, tái cấu trúc đau đớn |
| Truy vấn cơ sở dữ liệu | ❌ Không | Thuộc lãnh thổ kiểm thử tích hợp |
| HTTP handlers | ⚠️ Hạn chế | Kiểm thử phân tích request và tuần tự hóa response; không phải logic bên trong |
| Chỉ đường vui (happy path) | ❌ Không bao giờ | Đường lỗi có nhiều bug hơn đường vui |

---

## Cấu Trúc Kiểm Thử — Sắp Xếp / Hành Động / Kiểm Tra

Mỗi kiểm thử tuân theo mô hình AAA với dòng trống giữa mỗi phần:

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

## Kiểm Thử Dạng Bảng

Với các hàm có nhiều trường hợp đầu vào → đầu ra, luôn sử dụng kiểm thử dạng bảng:

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

## Yêu Cầu Độ Phủ

| Package | Độ phủ tối thiểu | Lý do |
|---------|-----------------|-------|
| `engine/parser` | 90% | Tính đúng đắn quan trọng — lỗi phân tích làm hỏng toàn bộ thực thi hạ nguồn |
| `engine/executor` | 85% | Logic phân nhánh phức tạp, nhiều chế độ thất bại |
| `engine/handlers/*` | 80% | Mỗi handler có thể kiểm thử độc lập và hướng tới khách hàng |
| `api/middleware` | 80% | Code quan trọng về bảo mật |
| `api/handlers` | 70% | Lớp HTTP; kiểm thử tích hợp phủ tốt hơn |
| `pkg/util/*` | 75% | Tiện ích dùng chung, nhiều nơi gọi |

Độ phủ được thực thi trong CI — PR không đạt ngưỡng sẽ không được merge.

```bash
# Kiểm tra độ phủ cục bộ
go test ./... -coverprofile=coverage.out
go tool cover -func=coverage.out | tail -1
# Phải hiển thị: total: (statements) XX.X%
```

---

## Các Dạng Sai Lầm Phổ Biến Cần Tránh

| Dạng sai lầm | Vấn đề | Sửa |
|-------------|--------|-----|
| `time.Sleep` trong kiểm thử | Làm kiểm thử chậm và bất ổn | Dùng `clock.Mock` hoặc đồng bộ bằng channel |
| Kiểm thử trực tiếp hàm private | Gắn chặt với triển khai | Kiểm thử qua API công khai; nếu logic private đủ phức tạp, hãy tách ra |
| Assert trên chuỗi thông báo lỗi chính xác | Dễ vỡ — thông báo thay đổi | Dùng `errors.Is()` hoặc kiểm tra kiểu lỗi |
| Một kiểm thử phủ nhiều hành vi | Khó debug khi thất bại | Một kiểm thử mỗi hành vi (dạng bảng là được) |
| Trạng thái có thể thay đổi dùng chung giữa kiểm thử | Phụ thuộc thứ tự, bất ổn | Mỗi kiểm thử tạo fixture riêng |
| `fmt.Println` debug còn sót trong kiểm thử | CI output nhiễu | Dùng `t.Logf` chỉ in khi thất bại |

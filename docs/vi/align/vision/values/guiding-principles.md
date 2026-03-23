# Nguyên Tắc Kỹ Thuật Định Hướng

> **Chủ sở hữu:** Văn phòng CTO | **Cập nhật lần cuối:** 2026-02-01

## Cách Chúng Tôi Xây Dựng

Những nguyên tắc này hướng dẫn các quyết định kỹ thuật hàng ngày. Khi đối mặt với sự đánh đổi, hãy tham khảo những nguyên tắc này trước khi leo thang.

---

### P1 — Công Nghệ Nhàm Chán Chiến Thắng

Chọn công nghệ bạn hiểu sâu thay vì công nghệ đang thú vị. PostgreSQL thay vì NewDB. Kafka thay vì hàng đợi tùy chỉnh. HTTP thay vì giao thức tùy chỉnh. Công nghệ nhàm chán có tài liệu, các chế độ lỗi đã được kiểm chứng, và một thị trường tuyển dụng.

> **Ngoại lệ:** Khi công nghệ nhàm chán chứng minh rõ ràng là không đủ (hiệu năng, quy mô, tính đúng đắn), chúng tôi khám phá các phương án thay thế bằng một bản proof of concept có giới hạn thời gian trước khi cam kết.

---

### P2 — Khả Năng Quan Sát Không Phải Tùy Chọn

Mọi dịch vụ phải có khả năng quan sát từ ngày đầu tiên:
- **Log:** JSON có cấu trúc, mọi request, mọi lỗi
- **Metrics:** Mô hình RED tối thiểu (Rate, Errors, Duration)
- **Traces:** Trace ID phân tán được lan truyền qua mọi cuộc gọi dịch vụ

Nếu bạn không thể debug trong production mà không cần `kubectl exec`, nó chưa sẵn sàng để giao.

---

### P3 — Thiết Kế Cho Thất Bại

Giả định mọi cuộc gọi bên ngoài sẽ thất bại. Giả định mọi ổ đĩa sẽ đầy. Giả định mọi dịch vụ sẽ khởi động lại giữa request.

| Mô hình | Khi nào áp dụng |
|---------|----------------|
| Circuit breaker | Bất kỳ cuộc gọi HTTP ra ngoài nào đến phụ thuộc không quan trọng |
| Retry với backoff | Lỗi tạm thời (mạng, giới hạn tốc độ) |
| Khóa idempotency | Bất kỳ thao tác ghi nào có thể được retry |
| Suy giảm uyển chuyển | Tính năng có thể hoạt động (với ít dữ liệu hơn) mà không cần phụ thuộc |
| Dead letter queue | Bất kỳ consumer hàng đợi tin nhắn nào |

---

### P4 — Rõ Ràng Hơn Ẩn Ý

Cấu hình phải rõ ràng. Giá trị mặc định phải được ghi chép. Phép thuật phải được tránh.

- Không có hành vi ẩn theo môi trường
- Không có `if ENV == 'production'` trong logic kinh doanh
- Không có chuyển đổi kiểu ngầm trong đầu vào API
- Các giá trị cấu hình ảnh hưởng đến hành vi production cần code review, không chỉ một cú nhấp trên dashboard

---

### P5 — Quyền Sở Hữu Rõ Ràng

Mọi hệ thống, dịch vụ, bảng dữ liệu, và API endpoint đều có người sở hữu được đặt tên. Những thứ không có chủ sẽ mục nát. Khi có sự cố lúc 3 giờ sáng, ai đó biết đó là vấn đề của họ phải sửa.

Sổ đăng ký quyền sở hữu được duy trì trong `CODEOWNERS` và danh mục dịch vụ tại `https://catalog.internal.apei.io`.

---

### P6 — Bảo Mật Là Tính Năng

Bảo mật không phải một giai đoạn hay một nhóm — đó là thuộc tính của mọi thứ chúng tôi xây dựng.

- Secret không bao giờ xuất hiện trong log, URL, hay thông báo lỗi
- Mọi đầu vào từ người dùng được xác thực và làm sạch trước khi xử lý
- Quyền tối thiểu là mặc định cho IAM roles, thông tin đăng nhập DB, và phạm vi API
- Endpoint mới yêu cầu mô hình đe dọa trong mô tả PR cho bất kỳ thao tác thay đổi dữ liệu nào

---

### P7 — Tự Động Hóa Lần Thứ Hai

Lần đầu tiên bạn làm thủ công, không sao. Lần thứ hai, hãy ghi chép lại. Lần thứ ba, hãy tự động hóa. Các quy trình thủ công xảy ra nhiều hơn một lần mỗi tháng nên có một ticket tự động hóa trong backlog.

---

### Khi Các Nguyên Tắc Xung Đột

Các nguyên tắc là heuristic, không phải luật. Khi hai nguyên tắc kéo theo hướng ngược lại, hãy sử dụng khung quyết định này:

1. Phạm vi ảnh hưởng nếu chúng ta sai là gì?
2. Quyết định này có thể đảo ngược trong vòng một ngày không?
3. Chúng ta sẽ nói gì với một kỹ sư mới gia nhập nhóm rằng quyết định này dạy họ về cách chúng tôi làm việc?

Câu trả lời cho (3) thường là lựa chọn đúng.

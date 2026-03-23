# Quản Lý Các Bên Liên Quan

Quản lý các bên liên quan đảm bảo đúng người được thông báo, tham vấn, và trao quyền trong suốt vòng đời APEI. Quản lý các bên liên quan kém là nguyên nhân hàng đầu gây ra lệch hướng dự án và bất ngờ ở giai đoạn cuối.

## Bản Đồ Các Bên Liên Quan

Các bên liên quan được phân loại theo mức độ ảnh hưởng và quan tâm:

```
            Ảnh hưởng cao
                 |
    Quản lý      |      Hợp tác
    chặt chẽ     |      chặt chẽ
                 |
  ───────────────┼─────────────────
                 |
    Giám sát     |      Thông báo
    (Tối thiểu)  |      thường xuyên
                 |
            Ảnh hưởng thấp

   Quan tâm thấp ←──────→ Quan tâm cao
```

### Phân Loại Các Bên Liên Quan

| Loại | Ảnh hưởng | Quan tâm | Chiến lược |
|------|----------|---------|-----------|
| **Người chủ chốt** | Cao | Cao | Hợp tác chặt chẽ, tham gia vào quyết định |
| **Người định hướng** | Cao | Thấp | Duy trì sự hài lòng, quản lý kỳ vọng |
| **Người tham gia** | Thấp | Cao | Thông báo thường xuyên, tận dụng sự nhiệt tình |
| **Đám đông** | Thấp | Thấp | Giám sát, giao tiếp tối thiểu |

## Ma Trận RACI

Ma trận RACI xác định ai là Người thực hiện (R), Người chịu trách nhiệm (A), Người được tham vấn (C), và Người được thông báo (I) cho mỗi hoạt động chính:

| Hoạt động | Product Owner | Tech Lead | Kỹ thuật | Thiết kế | QA | Các bên liên quan |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| Xác định yêu cầu | A | C | C | C | I | R |
| Quyết định kiến trúc | I | A | R | I | C | I |
| Lập kế hoạch Sprint | A | R | R | C | C | I |
| Thiết kế UI/UX | C | I | I | A/R | C | C |
| Triển khai code | I | R | A/R | I | I | I |
| Kiểm thử & QA | I | C | C | I | A/R | I |
| Phê duyệt phát hành | A | R | I | I | R | C |
| Hồi cố | R | R | R | R | R | I |
| Quyết định ngân sách | C | I | I | I | I | A |

**Chú giải:**
- **R** = Responsible (thực hiện công việc)
- **A** = Accountable (người ra quyết định cuối cùng)
- **C** = Consulted (cung cấp ý kiến trước quyết định)
- **I** = Informed (được thông báo sau quyết định)

## Kế Hoạch Giao Tiếp

### Nhịp Độ Giao Tiếp

| Đối tượng | Kênh | Tần suất | Nội dung | Chủ sở hữu |
|----------|------|---------|---------|-----------|
| Nhà tài trợ điều hành | Email tóm tắt | Hàng tuần | Tiến độ, rủi ro, quyết định cần thiết | Quản lý dự án |
| Các bên liên quan chính | Họp ban chỉ đạo | Hai tuần/lần | Rà soát trạng thái, cập nhật lộ trình | Product Owner |
| Nhóm phát triển | Standup | Hàng ngày | Rào cản, tiến độ, chuyển giao | Scrum Master |
| Tất cả các bên liên quan | Bản tin | Hàng tháng | Điểm nhấn, thành tựu, thay đổi sắp tới | Trưởng truyền thông |
| Đối tác bên ngoài | Rà soát hàng quý | Hàng quý | Lộ trình, cập nhật tích hợp | Quản lý đối tác |

### Mẫu Giao Tiếp

**Cập Nhật Trạng Thái Hàng Tuần:**

```markdown
## Trạng thái hàng tuần: [Tên dự án]
**Giai đoạn**: [Khoảng thời gian]
**Trạng thái tổng thể**: 🟢 Đúng tiến độ / 🟡 Có rủi ro / 🔴 Lệch tiến độ

### Điểm nổi bật
- [Thành tựu chính 1]
- [Thành tựu chính 2]

### Rủi ro & Vấn đề
| Rủi ro | Tác động | Biện pháp giảm thiểu | Chủ sở hữu |
|--------|---------|---------------------|-----------|

### Quyết Định Cần Thiết
- [ ] [Quyết định 1 — cần trước NGÀY]

### Trọng Tâm Tuần Tới
- [Ưu tiên 1]
- [Ưu tiên 2]
```

## Mức Độ Gắn Kết Các Bên Liên Quan

Theo dõi mức độ gắn kết của mỗi bên liên quan theo thời gian:

| Bên liên quan | Vai trò | Gắn kết hiện tại | Gắn kết mục tiêu | Hành động cần thiết |
|-------------|--------|:---:|:---:|----------------|
| VP Engineering | Nhà tài trợ | Ủng hộ | Nhà vô địch | Mời tham dự các buổi demo |
| Product Director | Người định hướng | Trung lập | Ủng hộ | Lên lịch họp 1:1 liên kết |
| Platform Team Lead | Chủ sở hữu phụ thuộc | Kháng cự | Ủng hộ | Giải quyết lo ngại tích hợp |
| Design Lead | Cộng tác viên | Ủng hộ | Ủng hộ | Duy trì nhịp độ hiện tại |
| Security Team | Người rà soát | Chưa biết | Được thông báo | Gửi tổng quan kiến trúc |
| Customer Success | Người ủng hộ | Nhà vô địch | Nhà vô địch | Tận dụng để thu thập phản hồi |

### Thang Đo Gắn Kết

1. **Chưa biết** — Không biết dự án tồn tại
2. **Kháng cự** — Biết nhưng phản đối hoặc lo ngại
3. **Trung lập** — Biết nhưng không gắn kết
4. **Ủng hộ** — Tích cực và sẵn sàng hỗ trợ khi được yêu cầu
5. **Nhà vô địch** — Chủ động ủng hộ và gỡ bỏ trở ngại

## Quản Lý Các Bên Liên Quan Khó Khăn

Khi gặp phải sự kháng cự:

1. **Lắng nghe trước**: Hiểu nguyên nhân gốc rễ của sự kháng cự trước khi phản hồi
2. **Tìm điểm chung**: Xác định mục tiêu chung giữa dự án và mối quan ngại của họ
3. **Cung cấp dữ liệu**: Sử dụng chỉ số và bằng chứng thay vì ý kiến để đưa ra lập luận
4. **Đề nghị tham gia**: Cho các bên liên quan kháng cự một vai trò có ý nghĩa để tăng quyền sở hữu
5. **Leo thang có xây dựng**: Nếu không thể liên kết, leo thang với bối cảnh được ghi chép tới một cấp có thẩm quyền chung

> **Nguyên tắc**: Mỗi lần tương tác với các bên liên quan là cơ hội để củng cố sự liên kết. Hãy coi giao tiếp là hoạt động chiến lược, không phải công việc hành chính.

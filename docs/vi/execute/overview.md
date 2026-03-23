# Tổng Quan — Giai Đoạn Thực Thi

Giai đoạn **Thực Thi** (Execute) là nơi kế hoạch trở thành hiện thực. Giai đoạn này tập trung vào việc giao hàng có kỷ luật thông qua các Sprint có cấu trúc, giao tiếp rõ ràng, và theo dõi liên tục so với kế hoạch.

## Khung Thực Thi

Khung thực thi APEI được xây dựng trên các trụ cột sau:

| Trụ cột | Mô tả | Thực hành chính |
|---------|-------|----------------|
| **Nhịp điệu** | Nhịp làm việc có thể dự đoán | Sprint, standup, review |
| **Khả kiến** | Mọi người có thể thấy tiến độ và rào cản | Dashboard, standup, cập nhật trạng thái |
| **Trách nhiệm** | Quyền sở hữu rõ ràng cho mọi nhiệm vụ | Người được giao, hạn chót, DoD |
| **Thích ứng** | Phản ứng với thay đổi mà không mất tập trung | Điều chỉnh Sprint, grooming backlog |

## Cấu Trúc Sprint

Chúng tôi sử dụng Sprint hai tuần làm đơn vị thực thi tiêu chuẩn:

```
Ngày 1  (Thứ Hai):  Lập kế hoạch Sprint (2 giờ)
Ngày 2-9:           Thực thi
Ngày 5  (Thứ Sáu):  Kiểm tra giữa Sprint (30 phút)
Ngày 10 (Thứ Sáu):  Sprint Review + Hồi cố (2 giờ)

Liên tục:
  - Standup hàng ngày: 15 phút, cùng giờ mỗi ngày
  - Refinement backlog: 1 giờ giữa Sprint
  - Lập trình đôi: khi cần
```

### Lập Kế Hoạch Sprint

Lập kế hoạch Sprint tuân theo định dạng có cấu trúc:

1. **Rà soát mục tiêu Sprint**: Câu nào mô tả thành công cho Sprint này?
2. **Lấy từ backlog đã ưu tiên**: Chọn story dựa trên năng lực và ưu tiên
3. **Phân chia task**: Chia story thành task 1-4 giờ mỗi cái
4. **Giao người phụ trách**: Mỗi task có đúng một người phụ trách
5. **Xác định rủi ro**: Điều gì có thể chặn chúng ta Sprint này?
6. **Cam kết**: Nhóm đồng ý về phạm vi Sprint

### Định Nghĩa Hoàn Thành

Một story được coi là "Hoàn thành" khi:

- [ ] Code đã viết và vượt qua tất cả unit test
- [ ] Code review đã được duyệt bởi ít nhất một đồng nghiệp
- [ ] Integration test vượt qua trong môi trường staging
- [ ] Tài liệu đã cập nhật (API docs, README, changelog)
- [ ] Product Owner đã chấp nhận story
- [ ] Không có regression đã biết được giới thiệu
- [ ] Feature flag đã cấu hình (nếu áp dụng)
- [ ] Giám sát và cảnh báo đã sẵn sàng cho chức năng mới

## Standup Hàng Ngày

Standup hàng ngày là nghi thức đồng bộ 15 phút:

**Định dạng mỗi người (tối đa 2 phút):**

1. Tôi đã hoàn thành gì từ standup trước?
2. Hôm nay tôi đang làm gì?
3. Có rào cản hoặc rủi ro nào không?

**Quy tắc:**

- Bắt đầu đúng giờ, kết thúc đúng giờ
- Đứng dậy (nếu trực tiếp) để giữ ngắn gọn
- Thảo luận chi tiết đưa vào "bãi đỗ" sau standup
- Cập nhật bảng task trước standup, không phải trong lúc
- Thành viên từ xa tham gia qua video với camera bật

## Theo Dõi Thực Thi So Với Kế Hoạch

### Kiểm Tra Sức Khỏe Hàng Tuần

Mỗi thứ Sáu, Scrum Master cập nhật dashboard sức khỏe Sprint:

| Chỉ số | Xanh | Vàng | Đỏ |
|--------|------|------|-----|
| Story hoàn thành vs. kế hoạch | >80% | 60-80% | <60% |
| Rào cản đang mở | 0 | 1-2 | 3+ |
| Thay đổi phạm vi Sprint này | 0 | 1 nhỏ | Bất kỳ lớn nào |
| Tinh thần nhóm (khảo sát) | >4.0 | 3.0-4.0 | <3.0 |
| Tỷ lệ build/deploy thành công | >95% | 85-95% | <85% |

### Khi Thực Thi Lệch Khỏi Kế Hoạch

Nếu kiểm tra sức khỏe hàng tuần cho thấy vàng hoặc đỏ:

1. **Chẩn đoán**: Đây là vấn đề phạm vi, năng lực, hay kỹ thuật?
2. **Giao tiếp**: Thông báo các bên liên quan trong vòng 24 giờ kể từ khi xác định rủi ro
3. **Điều chỉnh**: Giảm phạm vi, kéo dài thời gian, hoặc bổ sung nguồn lực (chọn tối đa hai)
4. **Ghi chép**: Ghi lại sai lệch và quyết định trong nhật ký Sprint
5. **Học hỏi**: Đưa insight trở lại giai đoạn Cải Tiến

## Các Dạng Sai Lầm Thực Thi

| Dạng sai lầm | Triệu chứng | Biện pháp |
|-------------|-----------|----------|
| Văn hóa anh hùng | Một người làm tất cả công việc quan trọng | Bắt buộc lập trình đôi và chia sẻ kiến thức |
| Phình phạm vi | Phạm vi Sprint tăng sau lập kế hoạch | Yêu cầu PO phê duyệt cho mọi bổ sung giữa Sprint |
| Quá tải họp | Kỹ sư có ít hơn 4 giờ tập trung/ngày | Kiểm toán cuộc họp, thiết lập khối giờ không họp |
| Rào cản im lặng | Rào cản không được nêu cho đến Sprint review | Tạo an toàn tâm lý để nêu vấn đề sớm |
| Mạ vàng | Kỹ thuật quá mức vượt yêu cầu | Tuân thủ nghiêm ngặt Định nghĩa Hoàn thành, không hơn |

> **Nguyên tắc**: Thực thi không phải là làm việc nhiều hơn; đó là làm việc có thể dự đoán. Một nhóm giao 80% kế hoạch một cách nhất quán có giá trị hơn một nhóm giao 120% Sprint này và 40% Sprint sau.

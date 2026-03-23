# Tổng Quan — Giai Đoạn Lập Kế Hoạch

Giai đoạn **Lập Kế Hoạch** (Plan) chuyển đổi sự liên kết thành công việc có thể hành động. Đây là nơi các mục tiêu chiến lược trở thành lộ trình, các mốc quan trọng, và phân chia công việc mà các nhóm có thể thực thi.

## Phương Pháp Lập Kế Hoạch

Khung APEI sử dụng phương pháp lập kế hoạch nhiều lớp:

| Lớp | Tầm nhìn thời gian | Mức độ chi tiết | Chủ sở hữu | Nhịp rà soát |
|-----|-------------------|----------------|-----------|-------------|
| Kế hoạch Chiến lược | 12 tháng | Chủ đề cấp cao | Lãnh đạo | Hàng quý |
| Lộ trình Hàng quý | 3 tháng | Epic và mốc quan trọng | Product + Engineering Leads | Hàng tháng |
| Kế hoạch Sprint | 2 tuần | Story và task | Nhóm giao hàng | Mỗi Sprint |
| Kế hoạch Hàng ngày | 1 ngày | Nhiệm vụ cá nhân | Cá nhân | Standup hàng ngày |

## Chu Kỳ Lập Kế Hoạch

Chu kỳ lập kế hoạch tiêu chuẩn diễn ra như sau:

```
Tuần 1: Thu thập đầu vào
  - Rà soát các sản phẩm liên kết từ giai đoạn Liên Kết
  - Thu thập nợ kỹ thuật và backlog bảo trì
  - Đánh giá năng lực và khả dụng của nhóm

Tuần 2: Soạn thảo và rà soát
  - Tạo lộ trình nháp với các mốc quan trọng
  - Xác định phụ thuộc và rủi ro
  - Rà soát với các bên liên quan để lấy phản hồi

Tuần 3: Hoàn thiện và truyền thông
  - Tích hợp phản hồi và điều chỉnh ưu tiên
  - Công bố lộ trình và kế hoạch Sprint chính thức
  - Truyền thông kế hoạch đến tất cả các bên liên quan

Tuần 4: Bắt đầu thực thi
  - Khởi động Sprint đầu tiên
  - Thiết lập dashboard theo dõi
  - Lên lịch các nghi thức định kỳ
```

## Sản Phẩm Lập Kế Hoạch Chính

Kết thúc giai đoạn Lập Kế Hoạch, bạn cần có:

- [ ] **Lộ trình hàng quý** với các mốc quan trọng và người phụ trách
- [ ] **Sprint backlog** cho Sprint đầu tiên
- [ ] **Bản đồ phụ thuộc** cho thấy phụ thuộc liên nhóm
- [ ] **Sổ đăng ký rủi ro** với chiến lược giảm thiểu
- [ ] **Kế hoạch năng lực** cho thấy phân bổ nhóm
- [ ] **Định nghĩa Hoàn thành (DoD)** được nhóm đồng thuận
- [ ] **Lịch giao tiếp** cho cập nhật đến các bên liên quan

## Từ Liên Kết Sang Lập Kế Hoạch

Quá trình chuyển đổi từ Liên Kết sang Lập Kế Hoạch tuân theo danh sách kiểm tra này:

| Bước | Mô tả | Trạng thái |
|------|-------|-----------|
| 1 | Tài liệu liên kết đã được ký duyệt | Bắt buộc |
| 2 | Mục tiêu và OKR đã được công bố | Bắt buộc |
| 3 | Bản đồ các bên liên quan đã hoàn thành | Bắt buộc |
| 4 | Đánh giá rủi ro ban đầu đã hoàn thành | Bắt buộc |
| 5 | Năng lực nhóm đã được xác nhận | Bắt buộc |
| 6 | Khả thi kỹ thuật đã được xác thực | Khuyến nghị |
| 7 | Ngân sách đã được phê duyệt | Bắt buộc |

## Nguyên Tắc Lập Kế Hoạch

1. **Lập kế hoạch ở mức chi tiết phù hợp**: Không lập kế hoạch quá chi tiết cho công việc ở tương lai xa. Sử dụng phương pháp chi tiết hóa dần — chi tiết tăng khi gần đến thực thi.

2. **Xây dựng vùng đệm**: Không kế hoạch nào tồn tại nguyên vẹn khi gặp thực tế. Dự trữ 15-20% năng lực cho công việc ngoài kế hoạch, lỗi, và chi phí vận hành.

3. **Làm rõ các phụ thuộc**: Nếu kế hoạch của bạn phụ thuộc vào nhóm khác giao sản phẩm, hãy ghi chép và xác nhận với họ. Các phụ thuộc giả định là nguồn thất bại kế hoạch lớn nhất.

4. **Lập kế hoạch cho các chế độ thất bại**: Với mỗi mốc quan trọng, hãy hỏi "Điều gì có thể sai?" và ghi chép phương án dự phòng.

5. **Giữ kế hoạch công khai**: Kế hoạch chỉ tồn tại trong công cụ quản lý dự án không phải là kế hoạch — đó là một mục trong cơ sở dữ liệu. Đảm bảo nhóm có thể trình bày kế hoạch từ trí nhớ.

## Hướng Dẫn Ước Lượng

| Kỹ thuật | Khi nào sử dụng | Độ chính xác |
|---------|-----------------|-------------|
| Phân loại áo (S/M/L/XL) | Các mục lộ trình giai đoạn đầu | Thấp, định hướng |
| Story points | Story cấp Sprint | Trung bình |
| Ước lượng theo thời gian | Nhiệm vụ được hiểu rõ | Cao (nếu có kinh nghiệm) |
| Ước lượng ba điểm | Công việc có độ không chắc chắn cao | Trung bình-Cao |

### Ước Lượng Ba Điểm

Với công việc không chắc chắn, sử dụng ước lượng lạc quan (O), nhiều khả năng nhất (M), và bi quan (P):

```
Kỳ vọng = (O + 4M + P) / 6
Độ lệch chuẩn = (P - O) / 6
```

> **Cảnh báo**: Kế hoạch là giả thuyết, không phải cam kết. Mục đích của kế hoạch là phối hợp hành động và cho phép học hỏi, không phải dự đoán tương lai với sự chắc chắn. Hãy sẵn sàng thích ứng khi có thông tin mới.

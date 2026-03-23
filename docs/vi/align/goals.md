# Mục Tiêu và OKR

Thiết lập mục tiêu hiệu quả là cầu nối giữa liên kết và hành động. Khung APEI sử dụng hệ thống phân cấp mục tiêu có cấu trúc để đảm bảo công việc cá nhân kết nối trực tiếp với chiến lược tổ chức.

## Khung Mục Tiêu SMART

Mỗi mục tiêu trong khung APEI phải đáp ứng tiêu chí SMART:

| Tiêu chí | Định nghĩa | Ví dụ |
|---------|-----------|-------|
| **S** - Cụ thể (Specific) | Xác định rõ ràng, không mơ hồ | "Giảm thời gian phản hồi API" chứ không phải "Cải thiện hiệu năng" |
| **M** - Đo được (Measurable) | Có chỉ số có thể định lượng | "Giảm p95 latency xuống dưới 200ms" |
| **A** - Khả thi (Achievable) | Thực tế với các ràng buộc hiện có | Phải tính đến quy mô nhóm và thời gian |
| **R** - Liên quan (Relevant) | Gắn với mục tiêu chiến lược | Phải ánh xạ tới ít nhất một OKR |
| **T** - Có thời hạn (Time-bound) | Có hạn chót rõ ràng | "Trước cuối Q2 2026" |

## Cấu Trúc OKR

Chúng tôi sử dụng Objectives and Key Results (OKR) làm cơ chế thiết lập mục tiêu chính:

### Ví Dụ OKR

**Mục tiêu 1: Cải thiện độ tin cậy nền tảng**

| Kết quả then chốt | Baseline | Mục tiêu | Trạng thái |
|-------------------|----------|---------|-----------|
| Giảm số sự cố mỗi tháng | 12 | 4 | Đúng tiến độ |
| Đạt SLA uptime 99,95% | 99,8% | 99,95% | Có rủi ro |
| Giảm thời gian trung bình khôi phục (MTTR) | 45 phút | 15 phút | Đúng tiến độ |

**Mục tiêu 2: Tăng tốc năng suất nhà phát triển**

| Kết quả then chốt | Baseline | Mục tiêu | Trạng thái |
|-------------------|----------|---------|-----------|
| Giảm thời gian CI/CD pipeline | 18 phút | 8 phút | Đúng tiến độ |
| Tăng tần suất triển khai | 2/tuần | 1/ngày | Chậm tiến độ |
| Giảm thời gian onboarding nhà phát triển mới | 3 tuần | 1 tuần | Đúng tiến độ |

## Phân Cấp Mục Tiêu

Mục tiêu chảy từ cấp tổ chức xuống đến cá nhân:

```
Mục tiêu Công ty (Hàng năm)
  └── Mục tiêu Phòng ban (Hàng quý)
       └── Mục tiêu Nhóm (Hàng quý)
            └── Mục tiêu Cá nhân (Sprint/Hàng tháng)
```

### Quy Tắc Phân Cấp

1. **Mỗi mục tiêu nhóm** phải ánh xạ tới ít nhất một mục tiêu phòng ban
2. **Mỗi mục tiêu cá nhân** phải ánh xạ tới ít nhất một mục tiêu nhóm
3. **Không có mục tiêu mồ côi**: Nếu mục tiêu không kết nối lên trên, hãy đặt câu hỏi về sự liên quan
4. **Giới hạn mục tiêu đang hoạt động**: Tối đa 3 mục tiêu với 3-5 kết quả then chốt mỗi nhóm mỗi quý

## Theo Dõi Mục Tiêu

### Định Dạng Cập Nhật Hàng Tuần

Mỗi tuần, người sở hữu mục tiêu cập nhật với:

- **Mức độ tự tin**: Cao / Trung bình / Thấp
- **Phần trăm tiến độ**: 0-100%
- **Rào cản**: Bất kỳ trở ngại nào ngăn cản tiến độ
- **Hỗ trợ cần thiết**: Yêu cầu cụ thể từ lãnh đạo hoặc các nhóm khác

### Rà Soát Hàng Tháng

| Hoạt động | Chủ sở hữu | Thời lượng |
|----------|-----------|-----------|
| Rà soát tiến độ mục tiêu | Trưởng nhóm | 30 phút |
| Cập nhật đánh giá rủi ro | Quản lý dự án | 15 phút |
| Kiểm tra phụ thuộc | Tech Lead | 15 phút |
| Điều chỉnh mục tiêu nếu cần | Trưởng nhóm + Nhà tài trợ | 15 phút |

## Bảng Mục Tiêu Mẫu

| ID | Mục tiêu | Chủ sở hữu | Hạn chót | Ưu tiên | Trạng thái |
|----|---------|-----------|---------|---------|-----------|
| G-001 | Ra mắt cổng onboarding tự phục vụ | @sarah | 2026-03-31 | P0 | Đang thực hiện |
| G-002 | Chuyển đổi xác thực sang OAuth 2.1 | @mike | 2026-04-15 | P0 | Đang lập kế hoạch |
| G-003 | Giảm 20% chi phí hạ tầng | @devops-team | 2026-06-30 | P1 | Đúng tiến độ |
| G-004 | Triển khai kiểm thử hồi quy tự động | @qa-team | 2026-05-15 | P1 | Có rủi ro |
| G-005 | Xuất bản tài liệu API công khai | @docs-team | 2026-04-30 | P2 | Chưa bắt đầu |

## Các Dạng Sai Lầm Cần Tránh

- **Mục tiêu phù phiếm**: Mục tiêu trông ấn tượng nhưng không thúc đẩy kết quả (ví dụ: "Viết 50 bài blog")
- **Dịch chuyển mục tiêu**: Thay đổi chỉ tiêu giữa quý mà không có lý do được ghi chép
- **Quá tải mục tiêu**: Hơn 5 mục tiêu đang hoạt động mỗi nhóm dẫn đến chuyển ngữ cảnh liên tục và mất tập trung
- **Chơi an toàn**: Đặt mục tiêu cố ý dễ để đảm bảo thành công làm mất đi mục đích của mục tiêu thách thức

> **Ghi nhớ**: Mục tiêu là công cụ giao tiếp cũng như công cụ theo dõi. Nếu nhóm không thuộc lòng ba mục tiêu hàng đầu, thì mục tiêu không phát huy tác dụng.

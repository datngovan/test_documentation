# Hồi Cố Nhóm Q1 2026

> **Ngày:** 20 tháng 3, 2026 | **Người điều phối:** Jordan Park | **Người tham dự:** Toàn bộ Nhóm Kỹ thuật (22)

## Định Dạng: Bắt Đầu / Dừng Lại / Tiếp Tục

---

## Bắt Đầu Làm

| Hạng mục | Phiếu bầu | Chủ sở hữu | Hành động |
|---------|----------|-----------|---------|
| Kiểm thử tải với dữ liệu quy mô production trong CI | 14 | Platform Team | Thêm kịch bản k6 cho workflow 10K-node vào CI pipeline trước Sprint 26-07 |
| Họp rà soát chỉ số hàng tuần (30 phút, toàn nhóm) | 11 | Jordan Park | Bắt đầu Sprint 26-06 — Thứ Hai 3PM |
| Lập trình đôi cho tính năng phức tạp (trên 2 SP) | 9 | Quy chuẩn nhóm | Thêm vào Definition of Ready: story > 8 SP yêu cầu kế hoạch pairing |
| Lập kế hoạch năng lực rõ ràng cho chi phí trực | 8 | Jordan Park | Dự trữ 15% năng lực mỗi Sprint cho công việc ngoài kế hoạch/trực |
| "Tài liệu quyết định kiến trúc" trước khi triển khai thay đổi lớn | 7 | Alice Chen | Mẫu đã tạo; sử dụng cho bất cứ thứ gì chạm vào engine hoặc mô hình dữ liệu |

---

## Dừng Lại Làm

| Hạng mục | Phiếu bầu | Nguyên nhân gốc | Sửa |
|---------|----------|----------------|-----|
| Triển khai vào thứ Sáu | 16 | Văn hóa "chỉ thêm một chút nữa" | Quy tắc cứng: không triển khai production sau 2PM thứ Năm |
| Bỏ qua post-mortem cho sự cố SEV-3 | 12 | "Không đủ nghiêm trọng" | Post-mortem nhẹ (30 phút, tài liệu bất đồng bộ) bắt buộc cho tất cả SEV-3+ |
| Merge PR không có mô tả | 10 | Áp lực thời gian | Mẫu PR được thực thi qua GitHub Actions — mô tả trống chặn CI |
| Thêm comment `TODO` mà không liên kết ticket | 8 | Ý định tốt, không theo dõi | Định dạng `TODO(ENG-XXXX)` bắt buộc; CI từ chối comment `TODO:` trống |
| Chạy kiểm thử hiệu năng thủ công | 7 | Không có phương án tự động | Sprint chặn: tự động hóa bộ benchmark trước cuối Q2 |

---

## Tiếp Tục Làm

| Hạng mục | Phiếu bầu | Tại sao hiệu quả |
|---------|----------|-----------------|
| Post-mortem không đổ lỗi cho SEV-1/2 | 18 | Niềm tin đã cải thiện; kỹ sư chia sẻ thông tin tự do trong sự cố |
| Họp 1:1 hàng tuần với skip-level (hàng quý) | 15 | Kỹ sư cảm thấy được lắng nghe; vấn đề nổi lên trước khi thành rủi ro giữ chân |
| Feature flags cho tất cả tính năng mới | 14 | Cho phép triển khai an toàn; vấn đề khách hàng phát hiện trong canary trước rollout đầy đủ |
| "Thứ Tư không họp" | 13 | Kỹ sư báo cáo trạng thái tập trung/flow cao nhất vào thứ Tư |
| Dashboard tiến độ OKR công khai | 11 | Mọi người biết chúng ta đang ở đâu; không bất ngờ tại QBR |

---

## Hành Động Hàng Đầu

| # | Hành động | Chủ sở hữu | Hạn chót | Xong? |
|---|---------|-----------|---------|-------|
| 1 | Thêm kiểm thử tải k6 10K-node vào CI | Platform | 14 tháng 4 (S26-07) | [ ] |
| 2 | Quy tắc cứng triển khai thứ Sáu — thêm vào sổ tay kỹ thuật | Jordan Park | 4 tháng 4 (S26-06) | [ ] |
| 3 | Triển khai thực thi mô tả PR trong GitHub Actions | Ivy Patel | 4 tháng 4 (S26-06) | [ ] |
| 4 | Bắt đầu họp rà soát chỉ số hàng tuần | Jordan Park | 30 tháng 3 (S26-06) | [ ] |
| 5 | Mẫu tài liệu quyết định kiến trúc — xuất bản + thông báo | Alice Chen | 27 tháng 3 | [x] Xong |
| 6 | Mẫu post-mortem nhẹ SEV-3 | Morgan Rivera | 4 tháng 4 (S26-06) | [ ] |

---

## Đo Lường Tâm Trạng

*Khảo sát ẩn danh trước hồi cố (thang điểm 1–5)*

| Câu hỏi | Điểm TB | Thay đổi so với Q4 |
|---------|---------|-------------------|
| Bạn hài lòng như thế nào với giao tiếp nhóm? | 4,1 | +0,3 |
| Bạn tự tin như thế nào về hướng kỹ thuật? | 4,4 | +0,6 |
| Khối lượng công việc có thể quản lý được không? | 3,4 | -0,2 |
| Nhóm xử lý thất bại tốt như thế nào? | 4,2 | +0,4 |
| Bạn có giới thiệu nhóm này cho bạn bè không? | 4,5 | +0,3 |

**Lưu ý:** Điểm khối lượng công việc giảm — phù hợp với 2 sự cố SEV-1 tiêu tốn nhiều ngày kỹ sư. Đầu tư ổn định nền tảng trong Q2 sẽ cải thiện điều này.

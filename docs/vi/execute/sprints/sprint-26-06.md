# Sprint 26-06 — Kế Hoạch và Tiến Độ

> **Sprint:** 23 tháng 3 – 4 tháng 4, 2026 | **Nhóm:** Core Engineering | **Năng lực:** 88 điểm

## Mục Tiêu Sprint

> *Hoàn thành tích hợp SSO doanh nghiệp cho AI Engine và giao bộ mẫu quy trình y tế v1 để nhóm không bị chặn cho GA.*

---

## Story Cam Kết

| ID | Tiêu đề | Điểm | Người thực hiện | Trạng thái |
|----|---------|------|----------------|-----------|
| ENG-1241 | Triển khai tích hợp Okta SAML cho AI Engine | 8 | Alice Chen | 🔄 Đang thực hiện |
| ENG-1242 | Thêm SCIM provisioning cho SSO doanh nghiệp | 5 | Alice Chen | 📅 Đã lên lịch |
| ENG-1243 | Y tế: mẫu quy trình tiếp nhận bệnh nhân | 3 | Dan Okafor | 📅 Đã lên lịch |
| ENG-1244 | Y tế: mẫu lịch hẹn khám | 3 | Dan Okafor | 📅 Đã lên lịch |
| ENG-1245 | Y tế: mẫu thông báo kết quả xét nghiệm | 3 | Dan Okafor | 📅 Đã lên lịch |
| ENG-1246 | Sửa rò rỉ bộ nhớ trong pipeline phân tích Flink | 5 | Bob Martinez | 🔄 Đang thực hiện |
| ENG-1247 | Nâng cấp Kafka lên 3.7.1 (bản vá bảo mật) | 3 | James Liu | ✅ Hoàn thành |
| ENG-1248 | Thêm cảnh báo SLO latency p99 cho workflow engine | 2 | Karen Singh | ✅ Hoàn thành |
| ENG-1249 | Tái cấu trúc plugin registry step handler (nợ kỹ thuật) | 8 | Carol Washington | 🔄 Đang thực hiện |
| ENG-1250 | Viết kiểm thử tải cho 10K thực thi đồng thời | 5 | Emily Zhao | 📅 Đã lên lịch |
| ENG-1251 | Mobile: sửa lỗi kết nối lại WebSocket Android | 5 | Henry Nakamura | 🔄 Đang thực hiện |
| ENG-1252 | Thêm import/export workflow (JSON) | 5 | Grace Kim | 📅 Đã lên lịch |
| ENG-1253 | Cập nhật API docs với các endpoint AI | 2 | Ivy Patel | 📅 Đã lên lịch |
| ENG-1254 | Kiểm toán dependency + cập nhật (dọn dẹp Q1) | 3 | Karen Singh | 📅 Đã lên lịch |
| **Tổng** | | **60** | | |

*28 điểm còn lại dành cho công việc ngoài kế hoạch (hỗ trợ, lỗi, trực)*

---

## Nhật Ký Standup Hàng Ngày

### Ngày 1 — 23 tháng 3

- **Alice:** Bắt đầu tích hợp SAML; phân tích metadata IdP hoạt động; đang xác thực assertion
- **Bob:** Tái tạo rò rỉ bộ nhớ Flink trong staging; heap dump cho thấy tích lũy không giới hạn trong window operator
- **James:** Nâng cấp Kafka hoàn thành trong staging; giám sát 24h trước khi đưa lên production
- **Rào cản:** Không có

### Ngày 2 — 24 tháng 3

- **Alice:** SAML hoạt động end-to-end với Okta sandbox; đang củng cố các đường dẫn lỗi
- **Bob:** Nguyên nhân gốc xác nhận: trạng thái window không bị thu hồi khi watermark vượt qua window; bản sửa trong PR #1891
- **James:** Kafka 3.7.1 đã đưa lên production; consumer lag bình thường
- **Karen:** Cảnh báo SLO p99 đã triển khai; test-firing đã xác nhận
- **Rào cản:** ENG-1249 bị chặn bởi design review — Carol cần 30 phút đồng bộ với Bob

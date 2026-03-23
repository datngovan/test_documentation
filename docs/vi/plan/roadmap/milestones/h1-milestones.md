# Theo Dõi Các Mốc H1 2026

> **Giai đoạn:** 1 tháng 1 — 30 tháng 6, 2026 | **Chủ sở hữu:** Lãnh đạo Kỹ thuật | **Cập nhật:** 2026-03-23

## Chú Giải Trạng Thái

| Ký hiệu | Ý nghĩa |
|---------|---------|
| ✅ | Hoàn thành |
| 🔄 | Đang thực hiện |
| ⚠️ | Có rủi ro |
| ❌ | Trượt |
| 📅 | Đã lên lịch |

---

## Các Mốc Q1

| Mốc | Chủ sở hữu | Hạn chót | Trạng thái | Ghi chú |
|-----|-----------|---------|-----------|---------|
| Chứng nhận SOC2 Type II | Bảo mật | 15 tháng 3 | ✅ | Đạt ngày 12 tháng 3 |
| Ra mắt beta AI Engine | Core Engine | 15 tháng 3 | ✅ | Ra mắt 12 tháng 3, hài lòng 94% |
| Chốt hợp đồng HealthFirst ($1,8M ACV) | Bán hàng | 31 tháng 3 | ✅ | Chốt ngày 18 tháng 3 |
| Tuyển 10 AE | Bán hàng | 31 tháng 3 | ⚠️ | 6/10 đã tuyển; 4 đang đàm phán |
| MTTR < 15 phút | SRE | 31 tháng 3 | ❌ | Đạt 18 phút; 2 sự cố SEV-1 làm chậm tiến độ |
| Không sự cố SEV-1 nào | SRE | 31 tháng 3 | ❌ | 2 sự cố SEV-1 trong Q1 |

**Tóm tắt Q1:** 4/6 mốc đạt được (67%). Mục tiêu doanh thu vượt; mục tiêu độ tin cậy trượt.

---

## Các Mốc Q2

| Mốc | Chủ sở hữu | Hạn chót | Trạng thái | Ghi chú |
|-----|-----------|---------|-----------|---------|
| AI Engine GA | Core Engine | 15 tháng 5 | 🔄 | Đúng tiến độ; SSO doanh nghiệp đang triển khai |
| Chứng nhận ISO 27001 | Bảo mật | 15 tháng 6 | 🔄 | Đánh giá khoảng cách trước kiểm toán ngày 1 tháng 4 |
| Ra mắt beta ứng dụng di động | Mobile | 1 tháng 6 | 🔄 | Tái thiết kế kiến trúc hoàn tất |
| Mẫu Y tế v1 (20 mẫu) | Sản phẩm | 1 tháng 5 | 📅 | Giai đoạn nghiên cứu |
| Hoàn thành tuyển dụng AE (còn 4) | Tuyển dụng | 30 tháng 4 | ⚠️ | 2 offer đang chờ; 2 chưa đưa ra |
| Thành lập pháp nhân EU | Pháp lý | 31 tháng 5 | 📅 | Đã thuê luật sư |
| Giảm 15% chi phí hạ tầng cloud | Platform | 30 tháng 6 | 🔄 | Đang rà soát reserved instance |
| NPS nhóm > 78 | HR | 30 tháng 6 | 📅 | Q1 đạt 76 |

---

## Các Phụ Thuộc Chính

```
AI Engine GA (15 tháng 5)
  └─ yêu cầu: Enterprise SSO (Okta/SAML) ←── Engineering (15 tháng 4)
  └─ yêu cầu: Kiểm thử tải 10K thực thi đồng thời ←── QA (1 tháng 5)

ISO 27001 (15 tháng 6)
  └─ yêu cầu: Khắc phục khoảng cách trước kiểm toán ←── Bảo mật (30 tháng 4)
  └─ yêu cầu: Đánh giá nhà cung cấp hoàn tất ←── Bảo mật (20 tháng 4)
  └─ yêu cầu: Đào tạo bảo mật nhân viên 100% ←── HR (15 tháng 4)

Pháp nhân EU (31 tháng 5)
  └─ yêu cầu: Thuê luật sư ←── Pháp lý ✅
  └─ yêu cầu: Địa chỉ đăng ký tại Dublin ←── Vận hành (30 tháng 4)
  └─ yêu cầu: Bổ nhiệm giám đốc ←── CEO (1 tháng 5)
```

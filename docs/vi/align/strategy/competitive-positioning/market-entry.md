# Chiến Lược Thâm Nhập Thị Trường

> **Chủ sở hữu:** Nhóm Chiến Lược | **Cập nhật lần cuối:** 2026-02-15

## Mô Hình Go-to-Market

Chúng tôi sử dụng mô hình GTM **nhà phát triển dẫn dắt, doanh nghiệp chốt deal**:

1. **Tiếp cận (Land)** — nhà phát triển phát hiện sản phẩm qua gói miễn phí, SDK mã nguồn mở, hoặc cộng đồng
2. **Mở rộng (Expand)** — nhóm áp dụng, mức sử dụng tăng tự nhiên trong tổ chức
3. **Chuyển đổi (Convert)** — ký hợp đồng doanh nghiệp khi đạt khối lượng sử dụng đủ lớn
4. **Phát triển (Grow)** — mở rộng sang các đơn vị kinh doanh và trường hợp sử dụng bổ sung

Mô hình này giảm CAC (không cần tiếp cận lạnh cho giai đoạn tiếp cận) đồng thời cho phép ký các hợp đồng ACV lớn ở giai đoạn chuyển đổi.

---

## Hồ Sơ Khách Hàng Mục Tiêu

### Hồ Sơ Khách Hàng Lý Tưởng (ICP)

| Thuộc tính | Hồ sơ |
|-----------|-------|
| **Quy mô công ty** | 200–5.000 nhân viên |
| **Ngành** | Y tế, Dịch vụ Tài chính, Công nghệ |
| **Mức độ trưởng thành kỹ thuật** | Có đội ngũ kỹ thuật (từ 10 kỹ sư trở lên) |
| **Đặc điểm đau** | Quy trình thủ công chiếm hơn 20% năng lực nhóm |
| **Quyền phê duyệt ngân sách** | VP Engineering hoặc VP Operations có thể phê duyệt dưới $200K |
| **Yếu tố kích hoạt mua hàng** | Yêu cầu tuân thủ, đóng băng tuyển dụng, hoặc tích hợp M&A |

### ICP Tiêu Cực (Không Nhắm Tới)

- Công ty có dưới 5 kỹ sư (quá nhỏ để tích hợp, tỷ lệ rời bỏ cao)
- Cơ quan chính phủ (chu kỳ mua sắm quá dài, chưa đạt FedRAMP)
- Công ty chỉ chạy on-premise (mô hình SaaS của chúng tôi không phù hợp)

---

## Trình Tự Thâm Nhập Theo Khu Vực

| Giai đoạn | Thị trường | Thời gian | Tiêu chí Tiến/Dừng |
|----------|----------|----------|-------------------|
| 1 | Bắc Mỹ (Mỹ, Canada) | Hiện tại | ✅ Đang hoạt động |
| 2 | Anh + Ireland | Q3 2026 | Tuân thủ GDPR hoàn tất, pháp nhân EU đã thành lập |
| 3 | DACH (Đức, Áo, Thụy Sĩ) | Q1 2027 | €1M ARR từ Giai đoạn 2, đã tuyển CSM nói tiếng Đức |
| 4 | ANZ (Úc, New Zealand) | Q2 2027 | 50 khách hàng từ Giai đoạn 2+3, hỗ trợ địa phương |
| 5 | APAC (Singapore, Nhật Bản) | 2028 | $5M ARR ngoài Bắc Mỹ |

---

## Chiến Lược Thay Thế Đối Thủ

### Đối Đầu WorkflowCorp (Đối Thủ Truyền Thống)

WorkflowCorp thắng về nhận diện thương hiệu và độ rộng hệ sinh thái. Chúng tôi thắng về:
- **Trải nghiệm nhà phát triển** — API-first, 10 phút để có giá trị vs. thiết lập nhiều ngày của họ
- **Khả năng AI** — tích hợp gốc, không phải gắn thêm
- **Giá cả** — thanh toán theo sử dụng, phù hợp tổ chức nhỏ; mức tối thiểu của WorkflowCorp là $60K/năm

**Kế hoạch thay thế:**
1. Tìm một nhà phát triển thất vọng trong tài khoản (thường ở nhóm không dùng WorkflowCorp)
2. Thắng một trường hợp sử dụng nhỏ (PoC 30 ngày, không cần IT tham gia)
3. Mở rộng trong nhóm, sau đó sang phòng ban
4. Xây dựng ROI: tính thời gian tiết kiệm × chi phí giờ kỹ sư
5. Đưa người ra quyết định kinh tế vào khi mức sử dụng vượt $5K/tháng

### Đối Đầu AutomateIQ (Đối Thủ AI-Native)

AutomateIQ là đối thủ tương tự nhất. Chúng tôi thắng về:
- **Độ tin cậy** — p99 latency của họ gấp 2,3 lần chúng tôi (dữ liệu benchmark công khai)
- **Tính năng doanh nghiệp** — RBAC, audit logs, SSO (họ thiếu cả ba)
- **Tư thế bảo mật** — Đã chứng nhận SOC2 Type II; họ thì chưa

**Thông điệp đối đầu trực tiếp:** "AutomateIQ tuyệt vời cho prototype. Chúng tôi được xây dựng cho production."

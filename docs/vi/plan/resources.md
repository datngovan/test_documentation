# Nguồn Lực và Năng Lực

Lập kế hoạch nguồn lực đảm bảo nhóm có đủ nhân sự, ngân sách, và công cụ cần thiết để thực thi lộ trình. Thiếu nguồn lực là lý do phổ biến nhất khiến kế hoạch thất bại.

## Vai Trò và Trách Nhiệm Nhóm

| Vai trò | Số lượng | Trách nhiệm | Báo cáo cho |
|--------|---------|-------------|------------|
| Product Owner | 1 | Ưu tiên hóa, quản lý bên liên quan, yêu cầu | VP Sản phẩm |
| Engineering Manager | 1 | Sức khỏe nhóm, tuyển dụng, cải tiến quy trình | Director of Engineering |
| Tech Lead | 1 | Kiến trúc, chất lượng code, quyết định kỹ thuật | Engineering Manager |
| Senior Engineers | 3 | Phát triển tính năng, hướng dẫn, code review | Tech Lead |
| Mid-level Engineers | 4 | Phát triển tính năng, sửa lỗi | Tech Lead |
| Junior Engineers | 2 | Phát triển tính năng, kiểm thử, tài liệu | Senior Engineers |
| UX Designer | 1 | Nghiên cứu người dùng, wireframe, prototype | Design Lead |
| QA Engineer | 2 | Lập kế hoạch kiểm thử, tự động hóa, kiểm thử hồi quy | QA Lead |
| DevOps Engineer | 1 | CI/CD, hạ tầng, giám sát | Tech Lead |
| Scrum Master | 1 | Các nghi thức, gỡ bỏ trở ngại, quy trình | Engineering Manager |

**Tổng quy mô nhóm: 17**

## Phân Bổ Ngân Sách

### Phân Bổ Ngân Sách Q2 2026

| Danh mục | Phân bổ | Đã chi | Còn lại | % Đã dùng |
|---------|---------|-------|---------|----------|
| Nhân sự (lương) | $850.000 | $283.000 | $567.000 | 33% |
| Hạ tầng cloud | $120.000 | $38.000 | $82.000 | 32% |
| Giấy phép phần mềm | $45.000 | $44.500 | $500 | 99% |
| Đào tạo & phát triển | $15.000 | $3.200 | $11.800 | 21% |
| Hỗ trợ nhà thầu | $60.000 | $0 | $60.000 | 0% |
| Dự phòng (10%) | $109.000 | $0 | $109.000 | 0% |
| **Tổng** | **$1.199.000** | **$368.700** | **$830.300** | **31%** |

### Cơ Hội Tối Ưu Chi Phí

- **Reserved instances**: Chuyển từ on-demand sang reserved cho workload ổn định (tiết kiệm ước tính: $18.000/quý)
- **Hợp nhất giấy phép**: Loại bỏ công cụ trùng lặp — ba nhóm dùng các giải pháp giám sát khác nhau
- **Thời điểm nhà thầu**: Trì hoãn thuê nhà thầu cho đến khi hoàn thành M2 để tập trung ngân sách vào các hạng mục trên đường tới hạn

## Công Cụ và Công Nghệ

### Công Cụ Phát Triển

| Danh mục | Công cụ | Mục đích | Chi phí giấy phép |
|---------|--------|---------|------------------|
| IDE | VS Code / JetBrains | Soạn thảo code | $0 / $15/tháng mỗi chỗ |
| Quản lý phiên bản | GitHub Enterprise | Quản lý mã nguồn | $21/người/tháng |
| CI/CD | GitHub Actions | Build, test, deploy | Bao gồm trong GH Enterprise |
| Quản lý dự án | Linear | Theo dõi issue, Sprint | $8/người/tháng |
| Tài liệu | Notion | Tài liệu nội bộ, wiki | $10/người/tháng |
| Thiết kế | Figma | Thiết kế UI/UX | $15/editor/tháng |
| Giao tiếp | Slack | Nhắn tin nhóm | $12,50/người/tháng |
| Giám sát | Datadog | APM, log, metrics | $23/host/tháng |
| Theo dõi lỗi | Sentry | Giám sát exception | $26/tháng (gói team) |
| Feature Flags | LaunchDarkly | Quản lý tính năng | $12/chỗ/tháng |

### Ngăn Xếp Công Nghệ

```yaml
Frontend:
  framework: React 19
  language: TypeScript 5.4
  styling: Tailwind CSS 4.0
  state: Zustand
  testing: Vitest + Playwright

Backend:
  runtime: Node.js 22 LTS
  framework: Fastify 5
  language: TypeScript 5.4
  database: PostgreSQL 16
  cache: Redis 7
  search: Elasticsearch 8

Infrastructure:
  cloud: AWS
  containers: ECS Fargate
  cdn: CloudFront
  dns: Route 53
  iac: Terraform
  monitoring: Datadog + PagerDuty
```

## Lập Kế Hoạch Năng Lực

### Năng Lực Nhóm — Q2 2026

| Thành viên | Vai trò | Khả dụng | Nghỉ phép dự kiến | Năng lực thực tế |
|-----------|--------|:---:|:---:|:---:|
| Alice Chen | Tech Lead | 100% | 5 ngày (tháng 5) | 92% |
| Bob Kumar | Senior Eng | 100% | 10 ngày (tháng 6) | 85% |
| Carol Park | Senior Eng | 80% (20% trực) | 0 ngày | 80% |
| Dan Olsen | Senior Eng | 100% | 5 ngày (tháng 4) | 92% |
| Eve Martinez | Mid Eng | 100% | 0 ngày | 100% |
| Frank Liu | Mid Eng | 100% | 10 ngày (tháng 5) | 85% |
| Grace Kim | Mid Eng | 50% (50% dự án khác) | 0 ngày | 50% |
| Henry Wu | Mid Eng | 100% | 5 ngày (tháng 6) | 92% |
| Ivy Singh | Junior Eng | 100% | 0 ngày | 100% |
| Jack Brown | Junior Eng | 100% | 5 ngày (tháng 4) | 92% |

### Rủi Ro Năng Lực

| Rủi ro | Tác động | Khả năng | Biện pháp giảm thiểu |
|--------|---------|:---:|---------------------|
| Grace bị kéo hoàn toàn sang dự án khác | Mất 50% một kỹ sư | Cao | Phân công trước công việc cho Eve làm dự phòng |
| Tuyển dụng vị trí Senior Eng bị trì hoãn | Giảm năng lực senior cả quý | Trung bình | Ưu tiên nhà thầu cho các nhiệm vụ M1 |
| Gánh nặng trực ngoài kế hoạch tăng | Mất 10-20% năng lực cho kỹ sư trực | Trung bình | Đầu tư giảm nhiễu cảnh báo Sprint này |
| Phụ thuộc người chủ chốt Alice cho auth | Điểm lỗi đơn lẻ | Cao | Phiên lập trình đôi để chia sẻ kiến thức |

> **Quy tắc chung**: Lập kế hoạch cho 70-80% năng lực sử dụng, không phải 100%. Phần còn lại hấp thụ công việc ngoài kế hoạch, họp, và chi phí chuyển ngữ cảnh. Nhóm lập kế hoạch ở 100% sử dụng liên tục trượt hạn chót.

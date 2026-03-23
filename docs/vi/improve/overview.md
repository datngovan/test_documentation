# Tổng Quan — Giai Đoạn Cải Tiến

Giai đoạn **Cải Tiến** (Improve) khép lại vòng lặp APEI bằng cách biến kinh nghiệm thực thi thành bài học tổ chức. Nếu không có cải tiến có chủ đích, các nhóm lặp lại cùng sai lầm và bỏ lỡ cơ hội tăng tốc.

## Triết Lý Cải Tiến Liên Tục

Giai đoạn Cải Tiến dựa trên ba niềm tin:

1. **Mọi quy trình đều có thể cải tiến.** Dù mọi thứ diễn ra tốt đến đâu, luôn có chỗ để làm tốt hơn.
2. **Cải tiến đòi hỏi hành động có chủ đích.** Học hỏi không tự động xảy ra — nó đòi hỏi phản ánh có cấu trúc, insight được ghi chép, và theo dõi các hành động.
3. **Cải tiến nhỏ tích lũy.** Cải thiện 1% mỗi Sprint tích lũy thành 26% trong một năm. Thay đổi lớn hiếm khi cần thiết.

## Chu Kỳ Cải Tiến

Giai đoạn Cải Tiến tuân theo chu kỳ có cấu trúc phản hồi lại giai đoạn Liên Kết:

```
    ┌──────────────────────────────────────────────┐
    │                                              │
    ▼                                              │
 QUAN SÁT       PHÂN TÍCH       HÀNH ĐỘNG      XÁC MINH
 Điều gì         Tại sao nó      Chúng ta sẽ    Nó có
 đã xảy ra?      xảy ra?         thay đổi gì?   hiệu quả?
 Thu thập dữ     Tìm nguyên      Triển khai     Đo lường
 liệu và         nhân gốc        thay đổi       kết quả
 phản hồi
    │                                              │
    │              ┌────────────┐                   │
    └──────────────┤ Phản hồi   ├───────────────────┘
                   │ về LIÊN KẾT│
                   └────────────┘
```

### Các Giai Đoạn Chu Kỳ

| Giai đoạn | Hoạt động | Sản phẩm | Thời lượng |
|----------|----------|---------|-----------|
| **Quan sát** | Thu thập chỉ số, thu thập phản hồi, rà soát sự cố | Chỉ số Sprint, kết quả khảo sát, báo cáo sự cố | Trong Sprint |
| **Phân tích** | Hồi cố, phân tích nguyên nhân gốc, rà soát xu hướng | Ghi chú hồi cố, tài liệu RCA | Cuối Sprint |
| **Hành động** | Ưu tiên cải tiến, giao người phụ trách, triển khai | Backlog cải tiến, thay đổi quy trình | Sprint tiếp theo |
| **Xác minh** | Đo lường tác động thay đổi, điều chỉnh khi cần | So sánh chỉ số trước/sau | Sprint sau triển khai |

## Vòng Phản Hồi

Khung APEI duy trì nhiều vòng phản hồi ở các quy mô thời gian khác nhau:

| Vòng | Tần suất | Đầu vào | Đầu ra | Chủ sở hữu |
|------|---------|--------|-------|-----------|
| Standup hàng ngày | Hàng ngày | Rào cản, tiến độ | Điều chỉnh ngay lập tức | Scrum Master |
| Hồi cố Sprint | Hai tuần/lần | Kinh nghiệm nhóm | Cải tiến quy trình | Scrum Master |
| Sprint review | Hai tuần/lần | Phần mềm hoạt động | Phản hồi bên liên quan | Product Owner |
| Rà soát chỉ số hàng tháng | Hàng tháng | KPI, dashboard | Phân tích xu hướng | Engineering Manager |
| Lập kế hoạch hàng quý | Hàng quý | Toàn bộ dữ liệu cải tiến | Điều chỉnh chiến lược | Lãnh đạo |
| Rà soát hàng năm | Hàng năm | Xu hướng cả năm | Thay đổi tổ chức | VP/Director |

## Từ Cải Tiến Trở Lại Liên Kết

Đầu ra có giá trị nhất của giai đoạn Cải Tiến là insight phản hồi lại giai đoạn Liên Kết:

### Những Gì Phản Hồi Về Liên Kết

- **Insight chiến lược**: "Khách hàng quan tâm độ tin cậy hơn tính năng mới" nên thay đổi ưu tiên liên kết
- **Bài học năng lực**: "Chúng ta liên tục ước lượng quá năng lực 15%" nên thay đổi giả định lập kế hoạch
- **Phát hiện kỹ thuật**: "Kiến trúc không hỗ trợ quy mô 10x" nên kích hoạt thảo luận chiến lược
- **Tín hiệu thị trường**: "Đối thủ X ra mắt tính năng khách hàng đang hỏi" nên thông tin cho lộ trình
- **Phản hồi nhóm**: "Kỹ sư kiệt sức do gánh nặng trực" nên thay đổi kế hoạch nguồn lực

### Cách Phản Hồi Insight

1. **Gắn thẻ các hạng mục cải tiến** mang tính chiến lược (không chỉ chiến thuật) trong hồi cố
2. **Duy trì nhật ký insight** tích lũy bài học chiến lược qua các Sprint
3. **Trình bày nhật ký insight** tại lập kế hoạch hàng quý như đầu vào cho giai đoạn Liên Kết
4. **Theo dõi insight nào** đã được hành động và insight nào bị hoãn (và tại sao)

## Chỉ Số Cải Tiến

Theo dõi chính quy trình cải tiến:

| Chỉ số | Mô tả | Mục tiêu |
|--------|-------|---------|
| Hạng mục cải tiến xác định mỗi Sprint | Số lượng hành động từ hồi cố | 3-5 |
| Hạng mục cải tiến hoàn thành mỗi Sprint | Số cải tiến hoàn thành | >70% đã xác định |
| Thời gian chu kỳ cải tiến | Ngày từ xác định đến triển khai | <14 ngày |
| Vấn đề lặp lại | Vấn đề tái phát sau khi "đã giải quyết" | 0 |
| Xu hướng hài lòng nhóm | Điểm hài lòng Sprint-over-Sprint | Tăng hoặc ổn định trên 4.0 |

> **Nguyên tắc**: Mục tiêu của giai đoạn Cải Tiến không phải tìm điều gì sai — mà là tìm điều gì có thể tốt hơn. Đặt khung cải tiến như cơ hội, không phải phê bình. Nhóm sợ hồi cố sẽ không cải tiến.

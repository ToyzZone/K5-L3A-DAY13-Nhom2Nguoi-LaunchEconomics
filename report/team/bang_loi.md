# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Minh Thông · Người gắn nhãn 2: Nguyễn Tuấn Phong (gắn trong 8 phút, không trao đổi; mỗi người commit bộ nhãn trong file cá nhân trước khi so).

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 2 | Ngữ cảnh | Hệ thống | ✗ | Hệ thống |
| 3 | Giới hạn hệ thống | Ngữ cảnh | ✗ | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | ✓ | Ngầm |
| 6 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 7 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 8 | Ngữ cảnh | Hệ thống | ✗ | Hệ thống |
| 9 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | ✓ | Ngầm |
| 13 | Do người dùng | Giới hạn hệ thống | ✗ | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | ✓ | Do người dùng |
| 15 | Hệ thống | Hệ thống | ✓ | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 17 | Ngầm | Ngầm | ✓ | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | ✓ | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | ✓ | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | ✓ | Hệ thống |

**Tỉ lệ đồng thuận:** 16 / 20 = 80% (đạt ngưỡng 80%).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu quy tắc, chốt bằng nhãn thống nhất.

- **Ca 2 — Hệ thống (không phải Ngữ cảnh):** trợ lý truyền sai tham số loại hàng cho tool là vi phạm thiết kế và làm tính thiếu tiền; ngữ cảnh chỉ dùng khi kết quả đúng thiết kế, ở đây kết quả đã sai.
- **Ca 3 — Ngữ cảnh (không phải Giới hạn hệ thống):** hệ thống vẫn xử lý được và làm đúng thiết kế (hoàn qua ví LogiX), chỉ là kỳ vọng của khách khác; giới hạn chỉ dùng khi không thể xử lý.
- **Ca 8 — Hệ thống (không phải Ngữ cảnh):** viện dẫn điều khoản không tồn tại là sai so với chính sách và đã lộ ra; không phải khách hiểu nhầm trên kết quả đúng.
- **Ca 13 — Giới hạn hệ thống (không phải Do người dùng):** yêu cầu thuộc sản phẩm bảo hiểm của đối tác, nằm ngoài phạm vi xử lý; không phải do khách nhập sai.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi sổ cái `ok` cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả `ok`; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | `ticket_reopened` có reason = so_tien mà `audit_sample_checked` thấy hoàn đúng chính sách; cảnh báo khi > 1% yêu cầu/tuần | Mẫu tin nhắn luôn ghi cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu`; cảnh báo khi > 5% yêu cầu/tuần trong phạm vi pilot, theo loại yêu cầu | Giữ cách chuyển kèm tóm tắt; đưa `quoc_te` ra khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào `trace` | Kế toán trưởng |

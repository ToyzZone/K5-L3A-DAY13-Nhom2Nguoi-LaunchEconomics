# Báo cáo cá nhân — NguyenMinhThong-2A202603637

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Thông
- MSSV: 2A202603637
- Email: 26ai.thongnm@vinuni.edu.vn
- GitHub: [ToyzZone](https://github.com/ToyzZone)
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người viết code (A, B, E1) · người gắn nhãn 1 (C) · người kiểm số cho D

Nhóm có 2 người, chia theo chủ file để mỗi người làm độc lập (chi tiết trong `AGENTS.md`). Người viết code đổi sau giờ giải lao: tôi làm A, B, E1 cùng Claude Code và tự đối chiếu từng con số với đáp án; D do `ntphong4044` làm. Nhờ vậy cả hai người đều tự chạy và kiểm được số.

## 2. Phần việc phụ trách

| Nhiệm vụ | Việc của tôi | File |
| --- | --- | --- |
| A (CP1) | Ba hàm A1, `mo_hinh` (A2), tách theo loại (A3), chi phí cố định (A4); điền bảng | `src/lab13.py`, `report/team/bang_chi_phi.md` |
| B (CP2) | 9 kịch bản B1, cặp B2, giới hạn chạy B3, xem lại 100% B4; điền bảng | `src/lab13.py`, `report/team/bang_chi_phi.md` |
| C (CP3) | Người gắn nhãn 1: gắn độc lập 20 ca vào mục 4 của file này, push trước khi so với người gắn nhãn 2 | file này |
| D (CP4) | Người kiểm số: tính lại năm câu D1 bằng công thức để đối chiếu với `nhiem_vu_D` | file này, mục 4 |
| E1–E2 (CP5) | Đặc tả và tính thử chỉ số, danh sách event, rủi ro kinh tế (lấy số từ bảng độ nhạy) | `src/lab13.py`, `report/team/chi_so.md` |
| Chung | Thông tin nhóm, vai và đóng góp | `TEAM.md` |

## 3. Đóng góp cụ thể

- A1, A2: ba phép thử ĐẠT (1,20 · 1,25 · 1,25); `mo_hinh` tính tử số trên mọi lần chạy kể cả lỗi, mẫu số chỉ đếm `thanh_cong`. Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ).
- Con số bất lợi cho hồ sơ: tính cả 222 yêu cầu nhân viên phải làm thay thì chi phí cả hệ thống là 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated], không phải 0,37×.
- A3, A4: quoc_te 22.515 đ = 1,88× [simulated], tỉ lệ ok lần 1/2/3 là 30,0% / 11,4% / 2,2% nên chạy lại không giúp; đề xuất phạm vi noi_dia + hang_nang. Cộng chi phí cố định: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng [simulated].
- B: bảng độ nhạy 9 kịch bản, xếp hạng làm lại > xem lại > lương; giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ [simulated]); xem lại 100% đẩy lên 0,98–1,03× [simulated].
- C: gắn nhãn 1 cho 20 ca; dựng `label_tool.html` (không chứa nhãn tham khảo) để cả hai người gắn nhãn dùng.
- D: kiểm số năm câu D1 bằng công thức so sánh hai tỉ lệ (cùng Claude Code), khớp đúng với `nhiem_vu_D` (mục 4). Nhãn thống nhất của bảng lỗi khớp 20/20 với nhãn tham khảo (đối chiếu sau khi cả hai bộ nhãn đã push).
- E1, E2: ba chỉ số tính thử (82,83% · 27,12% · 4,25%), danh sách event có `trace_id`, 4 dòng rủi ro kinh tế lấy số từ bảng độ nhạy.

## 4. Bằng chứng

Commit trên `main`:

| Commit | Nội dung |
| --- | --- |
| abf393e | A1: ba hàm, ba phép thử ĐẠT |
| 93a11bd | A2: `mo_hinh`, bảng A1 và A2 |
| acb4681 | A3, A4: tách theo loại, tỉ lệ ok theo lần thử, chi phí cố định |
| 75e04ba | B1–B4: bảng độ nhạy, assert tự kiểm tra tuyến tính |
| 7a43783 | E1, E2: `nhiem_vu_E1`, `chi_so.md` |
| d1ca225 | Rút câu trả lời A, B về một dòng mỗi câu; ngưỡng E2 có số tính thử |
| 544119e, ee16765 | `TEAM.md` |
| b41de90 | `label_tool.html` |
| e55253c | Nhãn 20 ca của người gắn nhãn 1 (15:19, trước khi so hai bộ nhãn) |

File: `src/lab13.py` (mọi hàm phía trên khối D1), `report/team/bang_chi_phi.md`, `report/team/chi_so.md`. Chạy `python3 lab13.py` trong `src/` để in lại mọi số.

### Nhãn 20 ca (người gắn nhãn 1, gắn độc lập)

Năm loại: Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm. Gắn theo nguyên nhân gốc. Commit và push bảng này trước khi xem nhãn của người gắn nhãn 2.

| Ca | Nhãn |
| --: | --- |
| 1 | Do người dùng |
| 2 | Ngữ cảnh |
| 3 | Giới hạn hệ thống |
| 4 | Giới hạn hệ thống |
| 5 | Ngầm |
| 6 | Do người dùng |
| 7 | Hệ thống |
| 8 | Ngữ cảnh |
| 9 | Do người dùng |
| 10 | Ngữ cảnh |
| 11 | Giới hạn hệ thống |
| 12 | Ngầm |
| 13 | Do người dùng |
| 14 | Do người dùng |
| 15 | Hệ thống |
| 16 | Ngữ cảnh |
| 17 | Ngầm |
| 18 | Ngữ cảnh |
| 19 | Giới hạn hệ thống |
| 20 | Hệ thống |

Sau khi so: trùng 16/20 = 80%, lệch ở ca 2, 3, 8, 13; nhóm chốt theo nhãn người gắn nhãn 2, quy tắc phân biệt trong `bang_loi.md`.

### Kiểm số D1

Tính lại bằng công thức so sánh hai tỉ lệ (sai số chuẩn gộp dưới H0, riêng dưới H1; alpha 0,05, power 0,8), không dùng statsmodels:

| Câu | `nhiem_vu_D` | Tính lại | Kết quả |
| --- | ---: | --- | --- |
| a · theo yêu cầu, 0,70 → 0,75 | 1.251 | 1.250,7 → 1.251 | khớp |
| b · theo nhân viên, m = 75 | 3.103 → 84 người | DE = 1 + 74 × 0,02 = 2,48; 1.251 × 2,48 = 3.103 → 42 người/nhóm, 84 | khớp, > 40 người: không đủ |
| c · 20 nhân viên mỗi nhóm | 1.000 | 20 / 0,02 = 1.000 | khớp, < 1.251 |
| d · 6 depot mỗi nhóm | 300 | 6 / 0,02 = 300 | khớp |
| e · mức chênh 6 điểm | 859, m ≥ 299 | 858,3 → 859; m ≥ 859 × 0,98 / (20 − 859 × 0,02) = 298,5 → 299 | khớp |

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề, đề xuất cách chia việc theo chủ file (`AGENTS.md`); viết code A1, A2, A3, A4, B, E1 trong `src/lab13.py`; điền `bang_chi_phi.md`, `chi_so.md`; đối chiếu số với đáp án tham khảo; tính lại D1 để kiểm số; dựng `label_tool.html`; sau khi cả hai bộ nhãn đã push, gợi ý quy tắc phân biệt cho 4 ca lệch (nhóm chốt theo nhãn người gắn nhãn 2) và rà soát hồ sơ nhóm.
- Cách kiểm tra: ba phép thử A1 phải ĐẠT; `nhiem_vu_B` có assert "giảm một nửa" = −½ "gấp đôi" và cặp B2 = tổng hai tác động; đối chiếu từng số với số tham khảo trong hướng dẫn chi tiết (A2, A3, A4, B1, B3, E1 khớp đúng; B4 với 15,3 phút ra 12.415 đ so với 12.414 đ vì dùng trung bình chưa làm tròn); D1 tính lại bằng công thức, khớp đúng.
- Không dùng AI để gắn nhãn 20 ca: nhãn ở mục 4 do tôi tự gắn bằng `label_tool.html`.

## 6. Tự đánh giá

- Hiểu được vì sao chi phí thật (4.472 đ [simulated]) gấp 16,3 lần hoá đơn token: giờ nhân viên chiếm 92,5%, nên pilot phải theo dõi tỉ lệ làm lại và xem lại chứ không phải giá token.
- Hiểu được hai chỗ dễ so sai: chi phí mỗi việc thành công thấp nhất (chạy 1 lần) không phải là rẻ nhất cho công ty (chạy 2 lần), và so với nhân viên phải dùng chi phí cả hệ thống (0,49×), không phải 0,37×.
- Khi gắn nhãn, tôi lệch 4/20 ca, chủ yếu vì gắn theo chỗ khách thấy sai thay vì nguyên nhân gốc (ca 2, 8: trợ lý làm sai thiết kế nhưng tôi gắn Ngữ cảnh). Lần sau hỏi trước "trợ lý có làm đúng thiết kế không" rồi mới chọn loại.
- Cần cải thiện: tự tay tính ít nhất một con số A2 mà không dùng AI trước khi đối chiếu, để chắc mình làm lại được khi không có công cụ.

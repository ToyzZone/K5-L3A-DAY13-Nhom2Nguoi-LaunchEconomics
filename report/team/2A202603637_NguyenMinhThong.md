# Báo cáo cá nhân — NguyenMinhThong-2A202603637

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Thông
- MSSV: 2A202603637
- Email: 26ai.thongnm@vinuni.edu.vn
- GitHub: [ToyzZone](https://github.com/ToyzZone)
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người viết code (A, B) · người gắn nhãn 1 (C)

Nhóm có 2 người, chia theo chủ file để mỗi người làm độc lập (chi tiết trong `AGENTS.md`). Người viết code đổi sau giờ giải lao (A, B do tôi viết, D do `ntphong4044` viết), nên cả hai người đều tự tay tính được số.

## 2. Phần việc phụ trách

| Nhiệm vụ | Việc của tôi | File |
| --- | --- | --- |
| A (CP1) | Viết ba hàm A1, `mo_hinh` (A2), tách theo loại (A3), chi phí cố định (A4); điền bảng | `src/lab13.py`, `report/team/bang_chi_phi.md` |
| B (CP2) | Viết 9 kịch bản B1, cặp B2, giới hạn chạy B3, xem lại 100% B4; điền bảng | `src/lab13.py`, `report/team/bang_chi_phi.md` |
| C (CP3) | Người gắn nhãn 1: gắn độc lập 20 ca vào mục 4 của file này, push trước khi xem nhãn của người gắn nhãn 2 | file này |
| E1–E2 (CP5) | Đặc tả và tính thử chỉ số, danh sách event, rủi ro kinh tế (lấy số từ bảng độ nhạy) | `report/team/chi_so.md` |
| Chung | Điền thông tin nhóm, vai và đóng góp | `TEAM.md` |

## 3. Đóng góp cụ thể

- Viết ba hàm A1 (1,20 · 1,25 · 1,25, ĐẠT) và `mo_hinh`: tử số tính mọi lần chạy kể cả lỗi, mẫu số chỉ đếm `thanh_cong`. Kết quả: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ).
- Thêm con số bất lợi để hồ sơ không so sai: tính cả 222 yêu cầu nhân viên phải làm thay thì chi phí cả hệ thống là 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated].
- A3: quoc_te 22.515 đ = 1,88× [simulated], tỉ lệ ok lần 1/2/3 là 30,0% / 11,4% / 2,2%, nên chạy lại không giúp; đề xuất phạm vi noi_dia + hang_nang. A4: cộng chi phí cố định → 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng [simulated].
- B: bảng độ nhạy 9 kịch bản, xếp hạng làm lại > xem lại > lương; giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ [simulated]); xem lại 100% đẩy lên 0,98–1,03× [simulated].
- E1, E2: ba chỉ số tính thử (82,83% · 27,12% · 4,25%), 10 event có `trace_id`, 4 dòng rủi ro kinh tế lấy số từ bảng độ nhạy.

## 4. Bằng chứng

Commit trên `main`:

| Commit | Nội dung |
| --- | --- |
| abf393e | A1: ba hàm, ba phép thử ĐẠT |
| 93a11bd | A2: `mo_hinh`, bảng A1 và A2 |
| acb4681 | A3, A4: tách theo loại, tỉ lệ ok theo lần thử, chi phí cố định |
| 75e04ba | B1–B4: bảng độ nhạy, assert tự kiểm tra tuyến tính |
| 7a43783 | E1, E2: `nhiem_vu_E1`, `chi_so.md` |
| 544119e | `TEAM.md` |

File: `src/lab13.py` (mọi hàm phía trên khối D1), `report/team/bang_chi_phi.md`, `report/team/chi_so.md`. Chạy `python3 lab13.py` trong `src/` để in lại mọi số.

### Nhãn 20 ca (người gắn nhãn 1, gắn độc lập)

Năm loại: Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm. Gắn theo nguyên nhân gốc. Commit và push bảng này trước khi xem nhãn của người gắn nhãn 2.

| Ca | Nhãn |
| --: | --- |
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |
| 10 | |
| 11 | |
| 12 | |
| 13 | |
| 14 | |
| 15 | |
| 16 | |
| 17 | |
| 18 | |
| 19 | |
| 20 | |

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Claude Code: đọc đề, chia việc theo chủ file (`AGENTS.md`), viết code A1, A2, A3, A4, B, E1 trong `src/lab13.py` và điền `bang_chi_phi.md`, `chi_so.md`.
- Cách kiểm tra: ba phép thử A1 phải ĐẠT; trong `nhiem_vu_B` có assert kiểm tra "giảm một nửa" = −½ "gấp đôi" và cặp B2 = tổng hai tác động; đối chiếu từng số với số tham khảo trong hướng dẫn chi tiết (A2, A3, B1, B3 khớp đúng; B4 với 15,3 phút ra 12.415 đ so với 12.414 đ vì dùng trung bình chưa làm tròn).
- Không dùng AI để gắn nhãn 20 ca: nhãn ở mục 4 do tôi tự gắn.

## 6. Tự đánh giá

...

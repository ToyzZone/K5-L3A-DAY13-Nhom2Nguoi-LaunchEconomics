# Báo cáo cá nhân — NguyenTuanPhong-2A202603712

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tuấn Phong
- MSSV: 2A202603712
- Email: 26ai.phongnt@vinuni.edu.vn
- GitHub: [ntphong4044](https://github.com/ntphong4044)
- Vai trong nhóm: người viết code phần D + gắn nhãn 2 (C) + giữ hồ sơ

Nhóm có 2 người, chia theo chủ file để mỗi người làm độc lập (chi tiết trong `AGENTS.md`). Người viết code đổi sau giờ giải lao (A, B do `ToyzZone` viết, D do tôi viết), nên cả hai người đều tự tay tính được số.

## 2. Phần việc phụ trách

| Nhiệm vụ | Việc của tôi | File |
| --- | --- | --- |
| D (CP4) | Viết hàm `nhiem_vu_D` (cỡ mẫu D1, năm câu tách tác động D2); tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại; điền `pilot_plan.yaml` (không còn dấu `?`, ≥ 3 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ) | `src/lab13.py` (khối `nhiem_vu_D`), `report/team/pilot_plan.yaml` |
| C (CP3) | Người gắn nhãn 2: gắn độc lập 20 ca vào mục 4 của file này, push trước khi xem nhãn của người gắn nhãn 1. Sau khi cả hai push: chép hai bộ nhãn vào `bang_loi.md`, tính đồng thuận, ghi quy tắc ca không trùng, điền bảng khắc phục 5 ca | file này, `report/team/bang_loi.md` |
| E3 (CP5) | Giữ hồ sơ: điền `ho_so_launch_v0.md` dần từ đầu buổi (mục 5, 6 điền ngay; các mục còn lại lấy số từ `bang_chi_phi.md` và `chi_so.md`); viết đề xuất cuối (Go / Go có điều kiện / No-go) | `report/team/ho_so_launch_v0.md` |
| Duyệt chéo (CP5) | Đọc hồ sơ nhóm hội đồng, chấm theo 3 tiêu chí, viết quyết định kèm lý do và một câu hỏi | `report/team/phieu_cham.md` |
| Chung | Viết báo cáo nhóm (mục khó khăn, cách xử lý) | `report/team/group_report.md` |

## 3. Đóng góp cụ thể

- **Phần D — `nhiem_vu_D` và `pilot_plan.yaml`:** tính cỡ mẫu năm cách chia (theo yêu cầu 1.251/nhóm; theo nhân viên DE 2,48 → 3.103, cần 84 người > 40, không đủ; 20 người/nhóm tối đa 1.000 < 1.251; 6 depot/nhóm tối đa 300; mức chênh 6 điểm m ≥ 299). Chọn chia theo nhân viên 20+20, chấp nhận mức chênh 6 điểm (ghi rõ power 0,64 ở mức 5 điểm). Tính tỉ lệ mở lại hiện tại 4,25% trước khi đặt ngưỡng dừng.
- **Phần C — `bang_loi.md`:** gắn nhãn độc lập 20 ca; chép hai bộ nhãn, tính đồng thuận, viết quy tắc phân biệt ca không trùng; điền bảng khắc phục 5 ca (mỗi loại một ca, có cách phát hiện đo được và một vai trò phụ trách).
- **Phần E3 — `ho_so_launch_v0.md`:** ghép bảy mục thành một trang; đề xuất cuối kèm điều kiện, người phụ trách, ngày kiểm tra.
- **Duyệt chéo — `phieu_cham.md`:** chấm nhóm hội đồng theo bằng chứng (điền tại buổi duyệt chéo).

## 4. Bằng chứng

Commit, file, bảng hoặc con số do tôi làm.

**Nhãn độc lập 20 ca lỗi (nhiệm vụ C, gắn trước khi xem nhãn của người kia):**

| Ca | Nhãn | Ca | Nhãn |
| --: | --- | --: | --- |
| 1 | Do người dùng | 11 | Giới hạn hệ thống |
| 2 | Hệ thống | 12 | Ngầm |
| 3 | Ngữ cảnh | 13 | Giới hạn hệ thống |
| 4 | Giới hạn hệ thống | 14 | Do người dùng |
| 5 | Ngầm | 15 | Hệ thống |
| 6 | Do người dùng | 16 | Ngữ cảnh |
| 7 | Hệ thống | 17 | Ngầm |
| 8 | Hệ thống | 18 | Ngữ cảnh |
| 9 | Do người dùng | 19 | Giới hạn hệ thống |
| 10 | Ngữ cảnh | 20 | Hệ thống |

Nhãn trên commit trước khi xem nhãn của người gắn nhãn 1 (bằng chứng gắn độc lập); sau khi so: trùng 16/20 = 80%, lệch ở ca 2, 3, 8, 13.

Commit chính của tôi trên `main`:

| Nội dung | File |
| --- | --- |
| Hàm `nhiem_vu_D` (cỡ mẫu D1, DE, m tối thiểu) | `src/lab13.py` |
| `pilot_plan.yaml` đầy đủ, hết dấu `?`, 3 luật dừng | `report/team/pilot_plan.yaml` |
| Nhãn độc lập 20 ca | file này |
| Bảng lỗi: hai bộ nhãn, đồng thuận 80%, bảng khắc phục 5 ca | `report/team/bang_loi.md` |
| Hồ sơ launch v0 bảy mục + đề xuất | `report/team/ho_so_launch_v0.md` |
| Báo cáo nhóm | `report/team/group_report.md` |

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề và `AGENTS.md`, viết hàm `nhiem_vu_D` trong `src/lab13.py`, điền `pilot_plan.yaml`, `bang_loi.md`, `ho_so_launch_v0.md`, `group_report.md`.
- Không dùng AI để gắn nhãn 20 ca: nhãn ở mục 4 do tôi tự gắn, commit trước khi xem nhãn của người kia.
- Cách tự kiểm tra: chạy `python -c "import pandas as pd, lab13; lab13.nhiem_vu_D(pd.read_csv('logix_requests.csv', keep_default_na=False))"`, đối chiếu với số tham khảo trong hướng dẫn chi tiết (1.251 · 3.103 · 1.000 · 300 · 859 · m≥299 · DE 6,96 · 4,25% · 3,97%, khớp đúng); `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` chạy không lỗi và không còn dấu `?`; `grep -rni production report/team` không in gì.

## 6. Tự đánh giá

Nắm được vì sao số cụm (không phải tổng số yêu cầu) quyết định cỡ mẫu khi chia theo cụm, và vì sao với 40 nhân viên phải chấp nhận mức chênh 6 điểm. Rút kinh nghiệm: luôn tính tỉ lệ hiện tại của chỉ số an toàn (mở lại 4,25%) trước khi đặt ngưỡng dừng, nếu không pilot sẽ bị dừng ngay tuần đầu.

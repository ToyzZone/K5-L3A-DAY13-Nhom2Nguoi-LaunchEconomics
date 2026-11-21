# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính. Mọi số tính từ cột `_simulated` ghi nhãn `simulated`.

## 1. Thông tin nhóm

- Tên nhóm: Nhom2Nguoi
- Lớp: L3A
- Thành viên: xem `TEAM.md` (Nguyễn Minh Thông 2A202603637, Nguyễn Tuấn Phong 2A202603712)

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN và bảo vệ trước hội đồng Gate 2a, trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào. Nhóm 2 người chia theo chủ file (`AGENTS.md`) để làm song song, push thẳng `main` không xung đột; đổi người viết code sau giải lao (A, B, E1 do Thông; D do Phong) để cả hai tự tay tính được số.

## 3. Giải pháp

- A (CP1) — chi phí mỗi việc thành công: hàm `mo_hinh` cộng mọi lần chạy (kể cả lỗi) rồi chia số việc thành công. Chi tiết: `bang_chi_phi.md`, `src/lab13.py`.
- B (CP2) — độ nhạy: gọi lại `mo_hinh` cho 9 kịch bản, 1 cặp, giới hạn chạy, xem lại 100%. Chi tiết: `bang_chi_phi.md`.
- C (CP3) — bảng lỗi: hai người gắn nhãn 20 ca độc lập rồi so. Chi tiết: `bang_loi.md`.
- D (CP4) — pilot: tính cỡ mẫu 5 cách, chọn chia theo nhân viên 20+20. Chi tiết: `pilot_plan.yaml`, hàm `nhiem_vu_D`.
- E (CP5) — chỉ số, event, rủi ro, hồ sơ: `chi_so.md`, `ho_so_launch_v0.md`.

## 4. Kết quả

- Chi phí mỗi việc thành công: 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu [simulated]; giờ nhân viên chiếm 92,5% chi phí [simulated].
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) [simulated].
- So với nhân viên tự làm: cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated].
- Chỉ số đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, lỗi lọt đến khách 4,25%.
- Bảng lỗi: đồng thuận 16/20 = 80%; bảng khắc phục 5 ca đủ năm loại.
- Pilot: chia theo nhân viên 20+20, mde 6 điểm, n 859/nhóm, DE 6,96, 20 cụm/nhóm, 3 luật dừng.
- Đề xuất cuối (`ho_so_launch_v0.md`): Go có điều kiện cho pilot noi_dia + hang_nang.
- Kết quả duyệt chéo nhận được từ hội đồng: (điền sau buổi duyệt chéo Gate 2a).

## 5. Khó khăn và cách xử lý

- `python lab13.py` dừng ở phép thử A1 cho tới khi hàm A1 xong; Phong chạy riêng phần D bằng `python -c "import pandas as pd, lab13; lab13.nhiem_vu_D(...)"` để không phải chờ.
- Cỡ mẫu: với 40 nhân viên không cách chia cụm nào đủ mẫu cho mức chênh 5 điểm; xử lý bằng cách chấp nhận mức chênh 6 điểm và ghi rõ power 0,64 nếu tác động thật là 5 điểm.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

- Nguyễn Minh Thông: A, B, E1–E2; gắn nhãn 1.
- Nguyễn Tuấn Phong: D, bảng lỗi C, E3, duyệt chéo; gắn nhãn 2 kiêm giữ hồ sơ.

## 7. Hạn chế và hướng cải thiện

- Số xem lại và làm lại là `_simulated`; pilot phải thay bằng phút đo thật sau tuần 1.
- Chỉ số đợt chạy thử không có nhóm đối chứng nên chưa kết luận trợ lý "nâng" chỉ số; pilot có đối chứng mới tách được tác động.
- Cách chia theo nhân viên chỉ đủ mẫu cho mức chênh 6 điểm; nếu cần 5 điểm phải tăng quy mô ngoài 40 nhân viên hiện có.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`).

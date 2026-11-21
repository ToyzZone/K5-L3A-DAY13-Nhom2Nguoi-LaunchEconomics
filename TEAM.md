# Team

## Thông tin nhóm

- Tên nhóm: Nhom2Nguoi (nhóm 2 người)
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/ToyzZone/K5-L3A-DAY13-Nhom2Nguoi-LaunchEconomics · `main` · commit chốt ghi khi nộp

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Minh Thông | 2A202603637 | 26ai.thongnm@vinuni.edu.vn | ToyzZone | Người viết code (A, B, E1) · người gắn nhãn 1 · người kiểm số cho D |
|   2 | Nguyễn Tuấn Phong | 2A202603712 | 26ai.phongnt@vinuni.edu.vn | ntphong4044 | Người viết code (D) · người gắn nhãn 2 kiêm giữ hồ sơ · người kiểm số cho A, B |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

Nhóm có 2 người nên mỗi người giữ hai vai. Việc chia theo chủ file để hai người làm song song: chi tiết trong [AGENTS.md](AGENTS.md).

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## NguyenMinhThong-2A202603637

### Phần việc phụ trách

- Nhiệm vụ A, B: `src/lab13.py` (A1, `mo_hinh`, `nhiem_vu_A3_A4`, `nhiem_vu_B`), `report/team/bang_chi_phi.md`
- Nhiệm vụ E1, E2: `nhiem_vu_E1` trong `src/lab13.py`, `report/team/chi_so.md`
- Người gắn nhãn 1 ở nhiệm vụ C; `TEAM.md`

### Đóng góp cụ thể

- Mô hình chi phí từ trace: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn chia số yêu cầu; chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× [simulated]
- Tách theo loại, đề xuất phạm vi noi_dia + hang_nang (quoc_te 1,88× [simulated], chạy lại không giúp); bảng độ nhạy B1–B4
- Ba chỉ số tính thử, 10 event có trace_id, 4 dòng rủi ro kinh tế

### Bằng chứng

- Commit trên `main`: abf393e (A1), 93a11bd (A2), acb4681 (A3, A4), 75e04ba (B), 7a43783 (E1, E2)
- Báo cáo cá nhân: [report/team/2A202603637_NguyenMinhThong.md](report/team/2A202603637_NguyenMinhThong.md)

## NguyenTuanPhong-2A202603712

### Phần việc phụ trách

- Nhiệm vụ D: `nhiem_vu_D` trong `src/lab13.py`, `report/team/pilot_plan.yaml`
- Nhiệm vụ C: người gắn nhãn 2, `report/team/bang_loi.md`
- Nhiệm vụ E3 và duyệt chéo: `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`, `report/team/group_report.md`

### Đóng góp cụ thể

- Phong điền

### Bằng chứng

- Báo cáo cá nhân: [report/team/2A202603712_NguyenTuanPhong.md](report/team/2A202603712_NguyenTuanPhong.md)

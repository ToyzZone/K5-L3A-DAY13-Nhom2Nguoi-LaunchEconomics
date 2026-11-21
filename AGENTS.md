# AGENTS.md · Lab 13, nhóm 2 người

Đọc file này trước khi làm. Đề bài, luật, cách chấm: [README.md](README.md), [RULES.md](RULES.md), [RUBRIC.md](RUBRIC.md), [CHECKPOINTS.md](CHECKPOINTS.md). Cài đặt và lệnh chạy: [src/README.md](src/README.md). Cách làm từng bước: [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).

## Ai làm gì

Mỗi file có đúng một **chủ**. Mỗi người chỉ sửa và commit file mình là chủ, nên hai người làm song song, push không xung đột.

| | Thông · `ToyzZone` | Phong · `ntphong4044` |
| --- | --- | --- |
| Nhiệm vụ | A, B, E1–E2 · gắn nhãn 1 ở C | D, C (bảng lỗi), E3, duyệt chéo · gắn nhãn 2 ở C |
| `src/lab13.py` | Mọi thứ phía trên dòng `# ---------- Nhiệm vụ D1`, và các dòng `TODO CP1`, `TODO CP2` trong `__main__` | Khối từ dòng `# ---------- Nhiệm vụ D1` đến trước `if __name__` (hàm `nhiem_vu_D`) |
| `report/team/` | `bang_chi_phi.md`, `chi_so.md` | `pilot_plan.yaml`, `bang_loi.md`, `ho_so_launch_v0.md`, `phieu_cham.md`, `group_report.md` |
| File khác | `TEAM.md`, `report/team/2A202603637_NguyenMinhThong.md` | File cá nhân `report/team/<MSSV>_<HoTenKhongDau>.md`, copy từ `MSSV_HoTen.md` (giữ nguyên file mẫu) |

Một nhiệm vụ xong khi mục "Tự kiểm tra" của checkpoint đó trong [CHECKPOINTS.md](CHECKPOINTS.md) đạt và file đã push.

## Chạy phần D khi phần A chưa xong

`python lab13.py` dừng ở phép thử A1 cho tới khi Thông viết xong A1. Phong chạy riêng phần D, trong thư mục `src/`:

```bash
python -c "import pandas as pd, lab13; lab13.nhiem_vu_D(pd.read_csv('logix_requests.csv', keep_default_na=False))"
```

## Gắn nhãn độc lập (nhiệm vụ C)

1. Mỗi người tự gắn nhãn 20 ca (mục "Hai mươi ca lỗi" trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`) vào mục 4 "Bằng chứng" của file cá nhân, commit và push, rồi mới mở nhãn của người kia hay bảng "Nhãn tham khảo" trong hướng dẫn chi tiết. Giờ commit là bằng chứng hai bộ nhãn độc lập.
2. Khi cả hai đã push, Phong chép hai bộ nhãn vào `bang_loi.md`, tính đồng thuận, ghi quy tắc cho ca không trùng, điền bảng khắc phục 5 ca.

## Chỗ phải chờ người kia

Ngoài ba chỗ dưới, mọi việc làm độc lập:

- `bang_loi.md`: chờ cả hai bộ nhãn đã push (mục trên).
- `pilot_plan.yaml`, trường `scope`: lý do thu hẹp phạm vi dùng tỉ lệ thành công theo `loai`, Phong tự tính từ `logix_requests.csv`; thêm tỉ số chi phí so với 12.000 đ khi bảng A3 trong `bang_chi_phi.md` đã có.
- `ho_so_launch_v0.md`, `group_report.md`: mục 5 và 6 của hồ sơ điền ngay; các mục còn lại lấy số từ `bang_chi_phi.md` và `chi_so.md` sau khi Thông push. Hai file này làm cuối cùng.

## Số liệu và ba lỗi dễ mất điểm

Mọi con số trong hồ sơ lấy từ output `src/lab13.py`, hoặc tính tay có ghi cách tính. Số trong hướng dẫn chi tiết là đáp án để đối chiếu (được lệch tối đa 2%).

- Số tính từ cột `_simulated` mang nhãn `simulated`.
- Người phụ trách là một vai trò cụ thể, ví dụ "PM trợ lý hoàn phí", "Giám đốc vận hành".
- Gọi đợt triển khai là "pilot" hoặc "đợt chạy thử"; `grep -rni production report/team` phải không in gì.

## Git

Làm thẳng trên `main`, chỉ `git add` file mình là chủ:

```bash
git pull --rebase origin main
git add <file của mình>
git commit -m "<mô tả ngắn>"
git push origin main
```

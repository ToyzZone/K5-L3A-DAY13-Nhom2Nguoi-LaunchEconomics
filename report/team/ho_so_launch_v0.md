# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhom2Nguoi · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc [simulated]; theo loại: noi_dia 2.696 đ (0,22×), hang_nang 8.221 đ (0,69×) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. số ca làm lại +51,8% · 2. tỉ lệ xem lại +40,7% · 3. lương nhân viên +23,1% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ; phạm vi noi_dia+hang_nang cộng cố định 4.599 đ = 0,38× [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, dùng, an toàn | Đợt chạy thử: chính 82,83% · bỏ qua gợi ý 27,12% · lỗi lọt đến khách 4,25% | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại, đồng thuận 80% (16/20); bảng khắc phục 5 ca, mỗi dòng có event + ngưỡng + một vai trò | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20+20, mde 6 điểm, n 859/nhóm, DE 6,96, 20 cụm/nhóm; 4 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ (hoàn trùng tách riêng, tắt ngay khi có 1 ca; ngưỡng chênh mở lại theo bước rollout 3,6 · 2,2 · 2 điểm) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 → 6.787 đ (+51,8%); xem lại 100% → 0,98–1,03×; cố định +1.185/+2.370 đ khi khối lượng giảm [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện — cho pilot phạm vi `noi_dia` + `hang_nang` (loại `quoc_te` 1,88× và `doi_tac` 0,85× [simulated]). Nêu con số bất lợi: với 40 nhân viên không cách chia cụm nào đủ mẫu cho mức chênh 5 điểm, nên chấp nhận mức chênh 6 điểm và power chỉ còn ~0,64 nếu tác động thật là 5 điểm; xem lại 100% thì chi phí lên 0,98–1,03× [simulated] nên gần như không tiết kiệm. Điều kiện:

- Sửa khoá chống trùng (ca 20) và đối soát sổ cái hoàn tiền (ca 7) — Kỹ sư trưởng agent — xong trước ngày bắt đầu pilot.
- Ký chấp nhận mức chênh 6 điểm (power 0,64 ở mức 5 điểm) — Giám đốc vận hành LogiX-VN — trước ngày bắt đầu pilot.
- Bật đủ 12 event có `trace_id` (danh sách trong `chi_so.md`); thay phút `_simulated` bằng phút đo thật — PM trợ lý hoàn phí — kiểm sau tuần 1.
- Kế hoạch giảm tỉ lệ xem lại theo bậc (vì xem lại 100% không tiết kiệm, B4) — Trưởng nhóm CSKH — kiểm cuối bước rollout 0,25.

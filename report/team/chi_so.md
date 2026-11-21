# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính thử in ra từ `nhiem_vu_E1` trong `src/lab13.py`. Số tiền ở E2 lấy từ `bang_chi_phi.md`, đều là simulated.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm có trợ lý được nhân viên mở bằng trợ lý | số `agent_suggestion_shown` chia số `refund_request_created` có `arm` = `tro_ly` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai số tiền trong mẫu kiểm tra hằng tuần (bắt lỗi ngầm mà khách không mở lại) | số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng. Ví dụ: chỉ số chính trong đợt chạy thử là 82,83%.

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent (`logix_runs.csv`).

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, arm, created_at, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | request_id, staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên | request_id, staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | request_id, phut_lam_lai, ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | request_id, reason, tom_tat, trace_id | Khi agent chuyển yêu cầu cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | request_id, idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| `ticket_closed` | Hệ thống ticket | request_id, closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | request_id, reopened_at, reason, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | request_id, so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, mẫu ngẫu nhiên |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `ticket_closed` (closed_at − created_at ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày; mẫu số là `refund_request_created`.
- Dùng, bỏ qua gợi ý: `staff_review_decision` có quyet_dinh là sua hoặc bo, chia tổng `staff_review_decision`.
- An toàn, lỗi lọt đến khách: `ticket_reopened` trong 7 ngày sau `ticket_closed`, chia `refund_request_created`.
- Dùng, tự đề xuất: `agent_suggestion_shown` chia `refund_request_created` có arm = tro_ly.
- An toàn, tự đề xuất: `audit_sample_checked` có so_tien_da_hoan ≠ so_tien_dung, chia số `audit_sample_checked`.
- Chi phí (để kiểm lại bảng độ nhạy trong pilot): token, tool từ `agent_run_completed`; phút xem lại từ `staff_review_decision`; phút làm lại từ `staff_rework_completed`; mẫu số từ `refund_ledger_write` có ket_qua thành công.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy (`bang_chi_phi.md`); mọi số tiền là simulated.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố mạnh nhất ở B1) | +51,8%, chi phí mỗi việc thành công lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần trong phạm vi > 7% (đợt chạy thử: 4,89%, 48/982), đo bằng `staff_rework_completed` | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất trước khi chạy tiếp | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] | Phút xem lại trung vị > 5 phút, hoặc tỉ lệ sửa + bỏ không giảm dưới 15% sau 2 tuần (đợt chạy thử: 27,12%) | Giảm tỉ lệ xem lại theo bậc chỉ khi sửa + bỏ < 15%; nếu không, dừng mở rộng | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa; vượt 12.000 đ dưới ~6.200 yêu cầu/tháng [simulated] | Số việc thành công theo tuần < 50% kế hoạch, đo bằng `refund_ledger_write` | Không mở rộng pilot, đàm phán lại chi phí cố định theo khối lượng | Giám đốc vận hành |
| Để giới hạn chạy lại 3 lần | Tốn hơn giới hạn 2 lần 136.365 đ trên 1.200 yêu cầu (7.037.585 so với 6.901.220 đ) [simulated] | Tỉ lệ ok của lần chạy thứ 3 < 20% theo tuần (đợt chạy thử: noi_dia 38,9%, hang_nang 17,9%), đo bằng `agent_run_completed` | Đặt giới hạn 2 lần, lần thứ 3 chuyển nhân viên | Trưởng nhóm kỹ thuật trợ lý |

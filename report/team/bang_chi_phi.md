# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT (= 1/p, k triệt tiêu) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool (5.600 lần gọi) | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại (890 phút) | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại (1.132 phút) | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | cộng bốn khoản trên | simulated (gồm xem lại, làm lại) |
| Số việc thành công | 978 | `ket_qua` == `thanh_cong` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | tổng chi phí / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần** (4.472 / 274,7) [simulated]: hoá đơn bỏ qua giờ nhân viên và chia cho cả việc không thành công.
- So với nhân viên tự làm phải dùng chi phí cả hệ thống, vì 4.472 đ chưa tính 222 yêu cầu không thành công (148 chuyển nhân viên, 74 làm lại) mà nhân viên phải làm thay: (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu = 0,49× của 12.000 đ** [simulated], không phải 0,37×.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại, 51,8%** [simulated], tiếp theo là xem lại 40,7% [simulated]; giờ nhân viên chiếm 92,5% tổng chi phí, token + tool chỉ 7,5%.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | So với 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- Loại nào không đáng để trợ lý xử lý? **quoc_te**: 22.515 đ = 1,88× nhân viên tự làm [simulated], chỉ 27,3% thành công.
- Chạy lại tới 3 lần không giúp: với quoc_te, tỉ lệ ok lần 1 là 30,0%, lần 2 chỉ 11,4%, lần 3 chỉ 2,2%; lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm tiền.
- doi_tac sát ngưỡng (0,85× [simulated], 54,4% thành công, lần 2 chỉ 18,2% ok) và có điều khoản riêng, nên cũng để ngoài phạm vi pilot; phạm vi đề xuất là noi_dia + hang_nang.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 3.414 + 1.185 = 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng (22.500) | 16.875 | 2.370 đ | 3.414 + 2.370 = 5.784 đ [simulated] | 0,48× [simulated] |

- Cách tính: việc thành công mỗi tháng = khối lượng × 900 / 1.200 (900 việc thành công của noi_dia + hang_nang trong mẫu 1.200); chi phí mỗi việc thành công trong phạm vi = 3.072.513 / 900 = 3.414 đ [simulated].
- Không đổi kết luận ở 45.000 hay 22.500 yêu cầu/tháng (0,38× và 0,48×), nhưng cố định tăng gấp đôi mỗi khi khối lượng giảm một nửa: dưới khoảng 6.200 yêu cầu/tháng (40.000.000 / ((12.000 − 3.414) × 0,75)) thì cps + cố định vượt 12.000 đ [simulated]. Hồ sơ phải ghi số đã cộng cố định và ở khối lượng nào.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công [simulated] | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Gốc (A2) | Tham số mặc định | 4.472 đ | |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

Tự kiểm tra (assert trong `nhiem_vu_B`): mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng 5,6% + 40,7% vì mô hình cộng tuyến tính (assert trong code).
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại (±51,8% / 25,9%) · 2. tỉ lệ xem lại (±40,7% / 20,3%) · 3. lương nhân viên (+23,1%) [simulated]. Giá token chỉ +5,6%, nên pilot phải theo dõi tỉ lệ làm lại và xem lại, không phải giá token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

Mọi cột tiền trong bảng B3 là simulated. Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay).

- **2 lần** rẻ nhất cho công ty (6.901.220 đ, ít hơn giới hạn 3 lần 136.365 đ) [simulated]. Không trùng: chi phí mỗi việc thành công thấp nhất ở 1 lần (4.111 đ), nhưng giới hạn đó đẩy thêm 85 yêu cầu sang nhân viên (319 so với 234) và tốn hơn 548.561 đ.

## B4 · Nếu phải xem lại tất cả

- Cách tính: 948 yêu cầu có lần chạy ok × 5 phút + 48 ca làm lại × 9 phút, nhân 2.000 đ, cộng token + tool 224.513 đ = 10.568.513 đ, chia 900 việc thành công → **11.743 đ = 0,98× của 12.000 đ** [simulated].
- Dữ liệu cho 15,3 phút mỗi ca làm lại (không phải 9 phút) → **12.415 đ = 1,03×** [simulated], tức đắt hơn nhân viên tự làm. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (làm lại 9 phút) hoặc ≤ 4,8 phút (làm lại 15,3 phút).
- Xem lại 100% thì trợ lý gần như không tiết kiệm được gì (tiền xem lại chiếm ~90% tổng). Pilot phải đo được tỉ lệ xem lại giảm an toàn xuống mức nào, và một lần xem lại có dưới 5 phút được không.

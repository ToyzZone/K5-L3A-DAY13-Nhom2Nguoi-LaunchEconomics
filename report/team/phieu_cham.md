# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Nhom2Nguoi (L3A)
- Nhóm được chấm: OPC (L3A) · github.com/anhdv282/K5-L3A-DAY13-OPC-LaunchEconomics · chấm trên commit `d8a8254`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 9 | Go có điều kiện khớp số của nhóm: phạm vi noi_dia + hang_nang cộng cố định 4.599 đ = 0,38×, cả hệ thống 5.865 đ = 0,49× [simulated]. Nêu cả hai con số bất lợi: xem lại 100% lên 0,98–1,03× [simulated], power 0,64 nếu tác động thật 5 điểm. Bốn điều kiện đều có vai trò và ngày kiểm tra (khoá chống trùng ca 7, 20; ký MDE 6 điểm; phút đo thật sau tuần 1; giảm xem lại theo bậc, mỗi lần ≤ 5 phút). Trừ 1 điểm: bảng kiểm số tính tay trong `bang_chi_phi.md` lệch 2,3–2,8% so với code và chưa ghi người tính, nên số A2 chưa được kiểm chéo độc lập |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 9 | Mọi số tiền trong hồ sơ, `chi_so.md`, `pilot_plan.yaml` có nhãn simulated (kể cả từng ô A3); ngưỡng 8.000 đ ghi rõ là ngưỡng quản trị, không phải số đo. Phạm vi thu hẹp có số: quoc_te 22.515 đ = 1,88×, thành công 27,3%, ok lần 1/2/3 = 30/11,4/2,2%; doi_tac 0,85× sát ngưỡng và có điều khoản riêng. Không dùng 0,37×. Trừ 1 điểm: `scope` ghi pilot "tại 12 depot", trong khi tỉ số 0,22× và 0,69× [simulated] chỉ đo ở 6 depot (D01–D06, 20 nhân viên) của đợt chạy thử; chưa nêu rủi ro khi ngoại suy sang 6 depot chưa có dữ liệu |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 9 | Chia theo nhân viên 20 + 20 (20 cụm mỗi nhóm, có đối chứng); nêu trần c/ICC = 1.000 < 1.251 nên chấp nhận mức chênh 6 điểm (859 mỗi nhóm, m ≥ 299, DE 6,96), nói rõ power ~0,64 nếu tác động thật 5 điểm và Giám đốc vận hành ký chấp nhận; ngưỡng an toàn +2 điểm so với đối chứng kèm trần 6% (không đặt 3% vì nền đã 4,25%); chỉ so lứa đủ cửa sổ 7 ngày, mỗi nhóm ≥ 100 yêu cầu, 2 lần đánh giá liên tiếp; hoàn trùng tách luật riêng, tắt ngay ≤ 30 phút; bốn luật dừng đủ bốn vế, rollback 30 phút. Trừ 1 điểm: ở bước 4 người, 100 yêu cầu cho sai số chuẩn ≈ √(0,04 × 0,96 / 100) ≈ 2 điểm, nên ngưỡng +2 điểm vẫn dễ tắt oan; nên nới ngưỡng theo bước rollout |
| **Tổng** | | | | **27 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Trong phạm vi pilot, chi phí là 0,38× mức 12.000 đ [simulated], và pilot chia 20 + 20 nhân viên tách được tác động. Hai con số bất lợi (xem lại 100% lên 0,98–1,03× [simulated], power 0,64 ở mức 5 điểm) đều có điều kiện xử lý, vai trò phụ trách và ngày kiểm tra. Lưu ý ngoài thang chấm: đồng thuận gắn nhãn chỉ 11/20 = 55% (nhóm đã nêu rõ và viết lại định nghĩa); bảng kiểm số tính tay còn lệch > 2% và chưa ghi người tính.

**Một câu hỏi cho đội trình:** Mỗi nhóm của pilot có bao nhiêu cụm, cỡ mẫu hiệu dụng tối đa là bao nhiêu? Nếu tác động thật chỉ 5 điểm thì pilot có bao nhiêu phần trăm cơ hội phát hiện ra? Và với tỉ lệ mở lại hiện tại 4,25%, ngưỡng an toàn của nhóm có làm pilot dừng ngay tuần đầu không?

**Câu trả lời của đội trình (ghi lại tại buổi):** Chia theo nhân viên 20 + 20; trần cỡ mẫu hiệu dụng c/ICC = 1.000 < 1.251 nên không đủ cho 5 điểm, chấp nhận mức chênh 6 điểm (859 mỗi nhóm, m ≥ 299 yêu cầu mỗi người, DE 6,96). Power ~0,64 nếu tác động thật 5 điểm, Giám đốc vận hành ký chấp nhận đánh đổi. Ngưỡng an toàn +2 điểm so với đối chứng kèm trần tuyệt đối 6%; không đặt trần 3% vì tỉ lệ hiện tại 4,25% (3,97% trong phạm vi) sẽ làm pilot dừng ngay tuần đầu. Luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ, người dừng là một vai trò cụ thể, rollback trong 30 phút.

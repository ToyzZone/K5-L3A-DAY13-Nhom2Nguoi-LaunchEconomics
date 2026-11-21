"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i = 1..k
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    # Tử số: mọi lần chạy, kể cả lần lỗi.
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    # Mẫu số: chỉ yêu cầu thành công.
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


# ---------- Nhiệm vụ A3, A4 · Tách theo loại, chi phí cố định ----------
PHAM_VI = ['noi_dia', 'hang_nang']
CO_DINH_THANG = 40_000_000
KHOI_LUONG_THANG = 45_000   # 1.500 yêu cầu/ngày × 30 ngày


def nhiem_vu_A3_A4(runs, reqs):
    print('\nA3 · loai        so_yc  ti_le_tc  lan_chay/yc       cps  /12000  [cps simulated]')
    for loai, nhom in reqs.groupby('loai'):
        kq = mo_hinh(runs, nhom)
        lan_chay = runs['request_id'].isin(nhom['request_id']).sum() / len(nhom)
        print(f'{loai:15s} {len(nhom):6d} {kq["thanh_cong"] / len(nhom):8.1%} {lan_chay:12.2f}'
              f' {kq["cps"]:9,.0f} {kq["cps"] / BASELINE:6.2f}x')
    # Chạy lại có giúp không: tỉ lệ lần chạy ok theo loại và theo lần thử.
    ok = runs.merge(reqs[['request_id', 'loai']]).assign(ok=lambda d: d['status'] == 'ok')
    print('\nTỉ lệ ok theo lần thử:')
    print(ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))

    pv = mo_hinh(runs, reqs[reqs['loai'].isin(PHAM_VI)])
    print(f'\nA4 · phạm vi {"+".join(PHAM_VI)}: {pv["thanh_cong"]} việc thành công, cps {pv["cps"]:,.0f} [simulated]')
    for ten, kl in [('đầy đủ', KHOI_LUONG_THANG), ('một nửa', KHOI_LUONG_THANG / 2)]:
        viec_thang = kl * pv['thanh_cong'] / len(reqs)
        co_dinh = CO_DINH_THANG / viec_thang
        print(f'{ten:8s} {kl:8,.0f} yc/tháng  {viec_thang:8,.0f} việc  cố định {co_dinh:6,.0f}'
              f'  cps+cố định {pv["cps"] + co_dinh:6,.0f} = {(pv["cps"] + co_dinh) / BASELINE:.2f}x')


# ---------- Nhiệm vụ B · Bảng độ nhạy (mọi cps ở đây là simulated) ----------
KICH_BAN = {
    'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
    'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
    'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
    'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
    'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
    'Lương tăng 25%':         dict(luong_phut=2500),
    'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
    'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
}


def nhiem_vu_B(runs, reqs):
    goc = mo_hinh(runs, reqs)['cps']
    doi = {ten: mo_hinh(runs, reqs, **kw)['cps'] / goc - 1 for ten, kw in KICH_BAN.items()}
    print(f'\nB1 · gốc {goc:,.0f}')
    for ten, d in doi.items():
        print(f'{ten:24s} {goc * (1 + d):8,.0f} {d:+7.1%}')
    # Tự kiểm tra: mô hình tuyến tính nên "giảm một nửa" = −½ "gấp đôi".
    for a, b in [('Giá token gấp đôi', 'Giá token giảm một nửa'), ('Xem lại gấp đôi', 'Xem lại giảm một nửa'),
                 ('Làm lại gấp đôi', 'Làm lại giảm một nửa')]:
        assert abs(doi[b] + doi[a] / 2) < 1e-9, (a, b)

    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps'] / goc - 1
    assert abs(cap - doi['Giá token gấp đôi'] - doi['Xem lại gấp đôi']) < 1e-9
    print(f'B2 · token × 2 + xem lại × 2: {goc * (1 + cap):,.0f} {cap:+.1%} (= tổng hai tác động riêng)')

    print('\nB3 · giới hạn  tổng trợ lý  không TC  cả hệ thống      cps')
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']   # nhân viên làm thay, 12.000 đ mỗi yêu cầu
        print(f'{k:>12d} {kq["tong"]:12,.0f} {khong_tc:9d} {kq["tong"] + khong_tc * BASELINE:12,.0f} {kq["cps"]:8,.0f}')

    # B4: xem lại 100% trong phạm vi; 5 phút mỗi yêu cầu có ít nhất một lần chạy ok, làm lại 9 phút mỗi ca (đề bài).
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    r = runs[runs['request_id'].isin(pv['request_id'])]
    co_ok = r.loc[r['status'] == 'ok', 'request_id'].nunique()
    ca_lam_lai = (pv['ket_qua'] == 'lam_lai').sum()
    may = (r['tokens_in'] / 1000 * GIA_VAO + r['tokens_out'] / 1000 * GIA_RA + r['tool_calls'] * GIA_TOOL).sum()
    thanh_cong = (pv['ket_qua'] == 'thanh_cong').sum()
    phut_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'\nB4 · {len(pv)} yc, {co_ok} có lần ok, {ca_lam_lai} ca làm lại, token+tool {may:,.0f}, {thanh_cong} thành công')
    for phut_lam_lai in (9, phut_tb):
        tong = co_ok * 5 * LUONG_PHUT + ca_lam_lai * phut_lam_lai * LUONG_PHUT + may
        hoa_von = (BASELINE * thanh_cong - may - ca_lam_lai * phut_lam_lai * LUONG_PHUT) / (co_ok * LUONG_PHUT)
        print(f'làm lại {phut_lam_lai:4.1f} phút: tổng {tong:,.0f}, cps {tong / thanh_cong:,.0f} = {tong / thanh_cong / BASELINE:.2f}x'
              f', hoà vốn khi xem lại ≤ {hoa_von:.1f} phút [simulated]')


# ---------- Nhiệm vụ E1 · Tính thử ba chỉ số ----------
def nhiem_vu_E1(reqs):
    chinh = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    mo_lai = reqs['mo_lai_trong_7_ngay'] == 1
    print(f'\nE1 · chính {chinh.mean():.2%} ({chinh.sum()}/{len(reqs)})'
          f' · dùng (bỏ qua gợi ý) {bo_qua.mean():.2%} ({bo_qua.sum()}/{len(xem)})'
          f' · an toàn (mở lại 7 ngày) {mo_lai.mean():.2%} ({mo_lai.sum()}/{len(reqs)})')
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    print(f'Tỉ lệ làm lại trong phạm vi {(pv["ket_qua"] == "lam_lai").mean():.2%}'
          f' · tỉ lệ được xem lại {reqs["duoc_xem_lai"].mean():.2%}')


# ---------- Nhiệm vụ D1 · Cỡ mẫu (ntphong4044 phụ trách, xem AGENTS.md) ----------
# TODO CP4: năm câu D1 và tỉ lệ mo_lai_trong_7_ngay hiện tại; in kết quả.
#   from statsmodels.stats.proportion import proportion_effectsize
#   from statsmodels.stats.power import NormalIndPower
def nhiem_vu_D(reqs):
    raise NotImplementedError('VIẾT Ở ĐÂY')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    nhiem_vu_A3_A4(runs, reqs)
    nhiem_vu_B(runs, reqs)
    nhiem_vu_E1(reqs)
    nhiem_vu_D(reqs)  # TODO CP4 · Nhiệm vụ D: viết trong hàm nhiem_vu_D ở trên.

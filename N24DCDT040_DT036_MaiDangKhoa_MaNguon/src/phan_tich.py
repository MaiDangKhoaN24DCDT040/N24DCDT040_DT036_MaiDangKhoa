"""DT036: quay lui theo tổng còn lại và chặn trên của số tiếp theo."""
def kiem_tra_phan_tich(b, n):
    """Không sửa b; trả False nếu sai kiểu, tổng, tính dương hay thứ tự."""
    return (type(n) is int and 1 <= n <= 20
            and isinstance(b, (list, tuple)) and len(b) > 0
            and all(type(x) is int and x > 0 for x in b)
            and sum(b) == n
            and all(b[i] >= b[i + 1] for i in range(len(b) - 1)))


def thu_phan_tich(con, lontoida, b, kq, dem, vet=None, k=None):
    """Hàm nội bộ. b hợp lệ; sum(b)+con=n; hoàn tác b sau mỗi nhánh."""
    dem['so_nut'] += 1
    dem['do_sau'] = max(dem['do_sau'], len(b))
    if vet is not None:
        vet.append(f"VAO con={con}, max={lontoida}, b={b}")
    if con == 0:
        if k is None or len(b) == k:
            kq.append(b.copy())  # Không giữ tham chiếu tới mảng đang quay lui.
            dem['so_phan_tu_ket_qua'] += len(b)
            if vet is not None:
                vet.append(f"GHI {b}")
        return
    if k is not None and len(b) >= k:
        return
    for v in range(min(con, lontoida), 0, -1):
        b.append(v)
        thu_phan_tich(con - v, v, b, kq, dem, vet, k)
        b.pop()
        if vet is not None:
            vet.append(f"LUI bo={v}, b={b}")


def phan_tich_so(n, *, lan_vet=False, k=None):
    """n thuộc 1..20. k tùy chọn: chỉ lấy nghiệm có đúng k số hạng."""
    if type(n) is not int or not 1 <= n <= 20:
        raise ValueError('n phải là số nguyên từ 1 đến 20')
    if k is not None and (type(k) is not int or not 1 <= k <= n):
        raise ValueError('k phải là số nguyên từ 1 đến n')
    kq = []
    dem = {'so_nut': 0, 'do_sau': 0, 'so_phan_tu_ket_qua': 0}
    vet = [] if lan_vet else None
    thu_phan_tich(n, n, [], kq, dem, vet, k)
    return {'nghiem': kq, 'so_cach': len(kq), 'dem': dem, 'vet': vet or []}

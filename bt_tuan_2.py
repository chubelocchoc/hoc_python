def lay_so_chan(ds: list[int]) -> list[int]:
    return [x for x in ds if x % 2 == 0]


def _nhap_danh_sach_so_nguyen() -> list[int]:
    s = input("Nhập danh sách số nguyên (cách nhau bởi khoảng trắng hoặc dấu phẩy): ").strip()
    if not s:
        return []

    s = s.replace(",", " ")
    parts = [p for p in s.split() if p]
    return [int(p) for p in parts]


def bai_1() -> None:
    ds = _nhap_danh_sach_so_nguyen()
    print("Danh sách số chẵn:", lay_so_chan(ds))


# -------------------- BÀI 2 --------------------
def nhap_diem_thi() -> dict[str, float]:
    lop: dict[str, float] = {}
    while True:
        ten = input("Nhập tên học sinh (Enter để dừng): ").strip()
        if ten == "":
            break
        try:
            diem = float(input("Nhập điểm: ").strip())
        except ValueError:
            print("Điểm không hợp lệ.")
            continue
        lop[ten] = diem
    return lop


def diem_trung_binh(lop: dict[str, float]) -> float | None:
    if not lop:
        return None
    return sum(lop.values()) / len(lop)


def hoc_sinh_max_min(lop: dict[str, float]) -> tuple[tuple[str, float] | None, tuple[str, float] | None]:
    if not lop:
        return (None, None)
    hs_max = max(lop.items(), key=lambda kv: kv[1])
    hs_min = min(lop.items(), key=lambda kv: kv[1])
    return (hs_max, hs_min)


def bai_2() -> None:
    lop = nhap_diem_thi()
    if not lop:
        print("Chưa có dữ liệu.")
        return

    dtb = diem_trung_binh(lop)
    hs_max, hs_min = hoc_sinh_max_min(lop)

    print("\n--- KẾT QUẢ ---")
    print("Danh sách:", lop)
    print(f"Điểm trung bình lớp: {dtb}")
    if hs_max:
        print(f"Cao nhất: {hs_max[0]} - {hs_max[1]}")
    if hs_min:
        print(f"Thấp nhất: {hs_min[0]} - {hs_min[1]}")


# -------------------- BÀI 3 --------------------
def dem_tu(van_ban: str) -> dict[str, int]:
    # Tách từ đơn giản theo khoảng trắng, chuẩn hoá chữ thường
    words = [w for w in van_ban.lower().split() if w]
    kq: dict[str, int] = {}
    for w in words:
        kq[w] = kq.get(w, 0) + 1
    return kq


def bai_3() -> None:
    vb = input("Nhập đoạn văn: ")
    print("Số lần xuất hiện mỗi từ:", dem_tu(vb))


# -------------------- BÀI 4 --------------------
def la_dict_long(d: dict) -> bool:
    return any(isinstance(v, dict) for v in d.values())


def bai_4() -> None:
    print("Nhập dictionary dạng Python, ví dụ: {'a': 1, 'b': {'c': 2}}")
    s = input("Dictionary: ").strip()
    try:
        d = eval(s, {"__builtins__": {}})
    except Exception:
        print("Không parse được dictionary.")
        return
    if not isinstance(d, dict):
        print("Giá trị nhập không phải dict.")
        return
    print("Dictionary lồng?" , la_dict_long(d))


# -------------------- BÀI 5 --------------------
def cong(a: float, b: float) -> float:
    return a + b


def tru(a: float, b: float) -> float:
    return a - b


def nhan(a: float, b: float) -> float:
    return a * b


def chia(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Không thể chia cho 0.")
    return a / b


def bai_5() -> None:
    while True:
        print("\n--- MÁY TÍNH BỎ TÚI ---")
        print("1) Cộng")
        print("2) Trừ")
        print("3) Nhân")
        print("4) Chia")
        print("0) Thoát")
        chon = input("Chọn (0/1/2/3/4): ").strip()
        if chon == "0":
            break
        try:
            a = float(input("Nhập a: "))
            b = float(input("Nhập b: "))
        except ValueError:
            print("Giá trị không hợp lệ.")
            continue

        try:
            if chon == "1":
                kq = cong(a, b)
            elif chon == "2":
                kq = tru(a, b)
            elif chon == "3":
                kq = nhan(a, b)
            elif chon == "4":
                kq = chia(a, b)
            else:
                print("Lựa chọn không hợp lệ.")
                continue
            print("Kết quả:", kq)
        except ZeroDivisionError as e:
            print("Lỗi:", e)


def main() -> None:
    while True:
        print("\n===== BT TUẦN 2 =====")
        print("1) Lấy các số chẵn trong list (list comprehension)")
        print("2) Quản lý điểm thi (dict) + trung bình + max/min")
        print("3) Đếm số lần xuất hiện của mỗi từ (dict)")
        print("4) Kiểm tra dictionary lồng")
        print("5) Máy tính bỏ túi (menu)")
        print("0) Thoát")
        chon = input("Chọn bài (0-5): ").strip()

        if chon == "0":
            break
        if chon == "1":
            bai_1()
        elif chon == "2":
            bai_2()
        elif chon == "3":
            bai_3()
        elif chon == "4":
            bai_4()
        elif chon == "5":
            bai_5()
        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()


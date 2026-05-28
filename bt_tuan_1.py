def _nhap_so_duong(thong_bao: str) -> float:
    while True:
        try:
            x = float(input(thong_bao))
            if x <= 0:
                print("Vui lòng nhập số > 0.")
                continue
            return x
        except ValueError:
            print("Giá trị không hợp lệ, hãy nhập một số.")


def _nhap_so_nguyen(thong_bao: str) -> int:
    while True:
        try:
            return int(input(thong_bao))
        except ValueError:
            print("Giá trị không hợp lệ, hãy nhập một số nguyên.")


def bai_tap_1() -> None:
    chieu_dai = _nhap_so_duong("Nhập chiều dài (cm): ")
    chieu_rong = _nhap_so_duong("Nhập chiều rộng (cm): ")

    dien_tich = chieu_dai * chieu_rong
    chu_vi = 2 * (chieu_dai + chieu_rong)

    print(f"Diện tích hình chữ nhật: {dien_tich} cm2")
    print(f"Chu vi hình chữ nhật: {chu_vi} cm")


def bai_tap_2() -> None:
    n = _nhap_so_nguyen("Nhập một số nguyên: ")
    if n % 2 == 0:
        print(f"{n} là số chẵn.")
    else:
        print(f"{n} là số lẻ.")


def tinh_tong_1_den_n(n: int) -> int:
    tong = 0
    for i in range(1, n + 1):
        tong += i
    return tong


def bai_tap_3() -> None:
    n = _nhap_so_nguyen("Nhập n (số nguyên dương): ")
    if n <= 0:
        print("n phải là số nguyên dương (> 0).")
        return
    print(f"Tổng các số từ 1 đến {n} là: {tinh_tong_1_den_n(n)}")


def bai_tap_4() -> None:
    danh_sach: list[dict] = []

    while True:
        print("\n--- QUẢN LÝ SINH VIÊN ---")
        print("1) Thêm sinh viên (tên + điểm)")
        print("2) In ra danh sách")
        print("3) Tìm sinh viên có điểm cao nhất")
        print("0) Thoát bài 4")
        chon = input("Chọn (0/1/2/3): ").strip()

        if chon == "0":
            break

        if chon == "1":
            ten = input("Nhập tên sinh viên: ").strip()
            if not ten:
                print("Tên không được để trống.")
                continue
            try:
                diem = float(input("Nhập điểm: "))
            except ValueError:
                print("Điểm không hợp lệ.")
                continue
            danh_sach.append({"ten": ten, "diem": diem})
            print("Đã thêm sinh viên.")

        elif chon == "2":
            if not danh_sach:
                print("Danh sách đang trống.")
                continue
            print("\nDanh sách sinh viên:")
            for i, sv in enumerate(danh_sach, start=1):
                print(f"{i}. {sv['ten']} - {sv['diem']}")

        elif chon == "3":
            if not danh_sach:
                print("Danh sách đang trống.")
                continue
            sv_max = max(danh_sach, key=lambda x: x["diem"])
            print(f"Sinh viên điểm cao nhất: {sv_max['ten']} - {sv_max['diem']}")

        else:
            print("Lựa chọn không hợp lệ.")


def la_palindrome(s: str) -> bool:
    s = s.strip()
    return s == s[::-1]


def bai_tap_5() -> None:
    s = input("Nhập chuỗi cần kiểm tra Palindrome: ")
    if la_palindrome(s):
        print(f"'{s}' là Palindrome.")
    else:
        print(f"'{s}' không phải Palindrome.")


def main() -> None:
    print("Bài tập 1: Tính diện tích & chu vi hình chữ nhật")
    print("Bài tập 2: Kiểm tra số chẵn hay lẻ")
    print("Bài tập 3: Tính tổng từ 1 đến n (loop)")
    print("Bài tập 4: Quản lý danh sách sinh viên")
    print("Bài tập 5: Kiểm tra chuỗi Palindrome")
    lua_chon = input("Chọn bài (1/2/3/4/5): ").strip()

    if lua_chon == "1":
        bai_tap_1()
    elif lua_chon == "2":
        bai_tap_2()
    elif lua_chon == "3":
        bai_tap_3()
    elif lua_chon == "4":
        bai_tap_4()
    elif lua_chon == "5":
        bai_tap_5()
    else:
        print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
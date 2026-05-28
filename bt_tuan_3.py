from __future__ import annotations


class NhanVien:
    def __init__(self, ten: str, luong: float, phong_ban: str) -> None:
        self.ten = ten
        self.luong = float(luong)
        self.phong_ban = phong_ban

    def tinh_thuong(self) -> float:
        # Thưởng 10% lương nếu lương > 20 triệu
        return 0.1 * self.luong if self.luong > 20_000_000 else 0.0


class SinhVien(NhanVien):
    def __init__(self, ten: str, luong: float, phong_ban: str, diem_trung_binh: float) -> None:
        super().__init__(ten=ten, luong=luong, phong_ban=phong_ban)
        self.diem_trung_binh = float(diem_trung_binh)

    def xep_loai(self) -> str:
        dtb = self.diem_trung_binh
        if dtb >= 8.5:
            return "Giỏi"
        if dtb >= 7.0:
            return "Khá"
        if dtb >= 5.0:
            return "Trung bình"
        return "Yếu"


class BankAccount:
    def __init__(self, so_tai_khoan: str, chu_tai_khoan: str, so_du: float = 0.0) -> None:
        self.so_tai_khoan = so_tai_khoan
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = float(so_du)

    def gui_tien(self, so_tien: float) -> None:
        so_tien = float(so_tien)
        if so_tien <= 0:
            raise ValueError("Số tiền gửi phải > 0.")
        self.so_du += so_tien

    def rut_tien(self, so_tien: float) -> None:
        so_tien = float(so_tien)
        if so_tien <= 0:
            raise ValueError("Số tiền rút phải > 0.")
        if so_tien > self.so_du:
            raise ValueError("Số dư không đủ để rút.")
        self.so_du -= so_tien

    def xem_so_du(self) -> float:
        return self.so_du


class Xe:
    def __init__(self, ten_xe: str, toc_do: float = 0.0, mau_sac: str = "") -> None:
        self.ten_xe = ten_xe
        self.toc_do = float(toc_do)
        self.mau_sac = mau_sac

    def tang_toc(self, delta: float) -> None:
        delta = float(delta)
        if delta < 0:
            raise ValueError("Delta tăng tốc phải >= 0.")
        self.toc_do += delta

    def giam_toc(self, delta: float) -> None:
        delta = float(delta)
        if delta < 0:
            raise ValueError("Delta giảm tốc phải >= 0.")
        self.toc_do = max(0.0, self.toc_do - delta)

    def __str__(self) -> str:
        return f"Xe(ten_xe='{self.ten_xe}', toc_do={self.toc_do}, mau_sac='{self.mau_sac}')"


class QuanLySinhVien:
    def __init__(self) -> None:
        self.danh_sach: list[SinhVien] = []

    def them(self, sv: SinhVien) -> None:
        self.danh_sach.append(sv)

    def xoa(self, ten: str) -> bool:
        ten_lower = ten.strip().lower()
        for i, sv in enumerate(self.danh_sach):
            if sv.ten.strip().lower() == ten_lower:
                del self.danh_sach[i]
                return True
        return False

    def tim_theo_ten(self, tu_khoa: str) -> list[SinhVien]:
        kw = tu_khoa.strip().lower()
        return [sv for sv in self.danh_sach if kw in sv.ten.strip().lower()]

    def in_danh_sach(self) -> None:
        if not self.danh_sach:
            print("Danh sách sinh viên trống.")
            return
        for i, sv in enumerate(self.danh_sach, start=1):
            print(f"{i}. {sv.ten} | DTB={sv.diem_trung_binh} | Xếp loại={sv.xep_loai()}")


def main() -> None:
    print("=== Demo Bài 1: NhanVien ===")
    nv = NhanVien("Anh A", 25_000_000, "Kế toán")
    print("Tên:", nv.ten, "| Lương:", nv.luong, "| Thưởng:", nv.tinh_thuong())

    print("\n=== Demo Bài 2: SinhVien kế thừa NhanVien ===")
    sv = SinhVien("Bạn B", 0, "SV", 8.2)
    print("Tên:", sv.ten, "| DTB:", sv.diem_trung_binh, "| Xếp loại:", sv.xep_loai())

    print("\n=== Demo Bài 3: BankAccount ===")
    tk = BankAccount("001234", "Bạn C", 1_000_000)
    tk.gui_tien(500_000)
    tk.rut_tien(200_000)
    print("Số dư:", tk.xem_so_du())

    print("\n=== Demo Bài 4: Xe ===")
    xe = Xe("Honda", 10, "Đỏ")
    xe.tang_toc(15)
    xe.giam_toc(5)
    print(xe)

    print("\n=== Demo Bài 5: QuanLySinhVien ===")
    ql = QuanLySinhVien()
    ql.them(SinhVien("Nguyễn Văn An", 0, "SV", 9.0))
    ql.them(SinhVien("Trần Thị Bình", 0, "SV", 6.8))
    ql.them(SinhVien("Lê Quốc Cường", 0, "SV", 4.5))
    ql.in_danh_sach()
    print("Tìm theo tên 'bình':", [x.ten for x in ql.tim_theo_ten("bình")])
    print("Xóa 'Lê Quốc Cường':", ql.xoa("Lê Quốc Cường"))
    ql.in_danh_sach()


if __name__ == "__main__":
    main()


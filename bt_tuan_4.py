from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, asdict


# =========================
# BÀI 1: Đọc file số liệu
# =========================
def doc_cac_so_tu_file(filename: str) -> list[float]:
    so: list[float] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            s = line.strip()
            if not s:
                continue
            try:
                so.append(float(s))
            except ValueError as e:
                raise ValueError(f"Dòng {line_no} không phải số hợp lệ: {s!r}") from e
    if not so:
        raise ValueError("File không có số nào hợp lệ.")
    return so


def bai_1() -> None:
    filename = input("Nhập tên file (mặc định data.txt): ").strip() or "data.txt"
    try:
        ds = doc_cac_so_tu_file(filename)
    except Exception as e:
        print("Lỗi:", e)
        return

    tong = sum(ds)
    tb = tong / len(ds)
    print("Tổng:", tong)
    print("Trung bình:", tb)
    print("Lớn nhất:", max(ds))
    print("Nhỏ nhất:", min(ds))


# =========================
# BÀI 2: Todo List (JSON)
# =========================
TODOS_FILE_DEFAULT = "todos.json"


@dataclass
class TodoItem:
    id: int
    title: str
    done: bool = False


def _load_todos(filename: str) -> list[TodoItem]:
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"File JSON bị lỗi định dạng: {filename}") from e

    if not isinstance(data, list):
        raise ValueError("todos.json phải là một list.")
    todos: list[TodoItem] = []
    for x in data:
        if not isinstance(x, dict):
            continue
        todos.append(
            TodoItem(
                id=int(x.get("id")),
                title=str(x.get("title", "")).strip(),
                done=bool(x.get("done", False)),
            )
        )
    return todos


def _save_todos(filename: str, todos: list[TodoItem]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in todos], f, ensure_ascii=False, indent=2)


def _next_todo_id(todos: list[TodoItem]) -> int:
    return (max((t.id for t in todos), default=0) + 1)


def _print_todos(todos: list[TodoItem]) -> None:
    if not todos:
        print("Danh sách công việc trống.")
        return
    for t in todos:
        status = "✅" if t.done else "❌"
        print(f"[{status}] #{t.id} - {t.title}")


def bai_2() -> None:
    filename = input(f"Nhập file todos (mặc định {TODOS_FILE_DEFAULT}): ").strip() or TODOS_FILE_DEFAULT
    try:
        todos = _load_todos(filename)
    except Exception as e:
        print("Lỗi:", e)
        return

    while True:
        print("\n--- TODO LIST ---")
        print("1) Thêm công việc")
        print("2) Xóa công việc")
        print("3) Đánh dấu hoàn thành")
        print("4) Hiển thị danh sách")
        print("0) Thoát")
        chon = input("Chọn (0-4): ").strip()

        if chon == "0":
            break

        if chon == "1":
            title = input("Nhập nội dung công việc: ").strip()
            if not title:
                print("Nội dung không được để trống.")
                continue
            todos.append(TodoItem(id=_next_todo_id(todos), title=title, done=False))
            _save_todos(filename, todos)
            print("Đã thêm.")

        elif chon == "2":
            try:
                todo_id = int(input("Nhập id cần xóa: ").strip())
            except ValueError:
                print("Id không hợp lệ.")
                continue
            before = len(todos)
            todos = [t for t in todos if t.id != todo_id]
            if len(todos) == before:
                print("Không tìm thấy id.")
            else:
                _save_todos(filename, todos)
                print("Đã xóa.")

        elif chon == "3":
            try:
                todo_id = int(input("Nhập id cần hoàn thành: ").strip())
            except ValueError:
                print("Id không hợp lệ.")
                continue
            found = False
            for t in todos:
                if t.id == todo_id:
                    t.done = True
                    found = True
                    break
            if not found:
                print("Không tìm thấy id.")
            else:
                _save_todos(filename, todos)
                print("Đã đánh dấu hoàn thành.")

        elif chon == "4":
            _print_todos(todos)
        else:
            print("Lựa chọn không hợp lệ.")


# ==========================================
# BÀI 3: Đếm tần suất từ (case-insensitive)
# ==========================================
def tan_suat_tu(words: list[str]) -> dict[str, int]:
    words_norm = [w.strip().lower() for w in words if str(w).strip() != ""]
    freq: dict[str, int] = {}
    for w in words_norm:
        freq[w] = freq.get(w, 0) + 1
    return freq


def bai_3() -> None:
    s = input("Nhập các từ (cách nhau bằng khoảng trắng): ").strip()
    words = [w for w in s.split() if w]
    print("Kết quả:", tan_suat_tu(words))


# ==================================
# BÀI 4: StudentManager (JSON + sort)
# ==================================
@dataclass
class Student:
    name: str
    gpa: float


class StudentManager:
    def __init__(self) -> None:
        self.students: list[Student] = []

    def load_from_file(self, filename: str) -> None:
        if not os.path.exists(filename):
            self.students = []
            return
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("File sinh viên phải là list JSON.")
        self.students = [Student(name=str(x["name"]), gpa=float(x["gpa"])) for x in data if isinstance(x, dict)]

    def save_to_file(self, filename: str) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([asdict(s) for s in self.students], f, ensure_ascii=False, indent=2)

    def add_student(self, name: str, gpa: float) -> None:
        self.students.append(Student(name=name.strip(), gpa=float(gpa)))

    def find_by_name(self, keyword: str) -> list[Student]:
        kw = keyword.strip().lower()
        return [s for s in self.students if kw in s.name.lower()]

    def get_top_students(self, n: int) -> list[Student]:
        n = int(n)
        if n <= 0:
            return []
        # sorted với key (lambda), giảm dần theo GPA rồi theo tên
        return sorted(self.students, key=lambda s: (-s.gpa, s.name.lower()))[:n]


def bai_4() -> None:
    filename = input("Nhập file sinh viên JSON (mặc định students.json): ").strip() or "students.json"
    sm = StudentManager()
    try:
        sm.load_from_file(filename)
    except Exception as e:
        print("Lỗi load:", e)
        return

    while True:
        print("\n--- STUDENT MANAGER ---")
        print("1) Thêm sinh viên")
        print("2) Tìm theo tên")
        print("3) Lấy top n")
        print("4) Lưu file")
        print("5) In danh sách")
        print("0) Thoát")
        chon = input("Chọn (0-5): ").strip()

        if chon == "0":
            break
        if chon == "1":
            name = input("Tên: ").strip()
            try:
                gpa = float(input("GPA: ").strip())
            except ValueError:
                print("GPA không hợp lệ.")
                continue
            sm.add_student(name, gpa)
            print("Đã thêm.")
        elif chon == "2":
            kw = input("Từ khóa: ").strip()
            kq = sm.find_by_name(kw)
            print([(s.name, s.gpa) for s in kq])
        elif chon == "3":
            try:
                n = int(input("Nhập n: ").strip())
            except ValueError:
                print("n không hợp lệ.")
                continue
            top = sm.get_top_students(n)
            print([(s.name, s.gpa) for s in top])
        elif chon == "4":
            sm.save_to_file(filename)
            print("Đã lưu.")
        elif chon == "5":
            print([(s.name, s.gpa) for s in sm.students])
        else:
            print("Lựa chọn không hợp lệ.")


# ==========================================
# BÀI 5: Word frequency từ file -> word_count
# ==========================================
WORD_RE = re.compile(r"[A-Za-zÀ-ỹ0-9_]+", flags=re.UNICODE)


def word_frequency_from_file(input_file: str) -> dict[str, int]:
    freq: dict[str, int] = {}
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            for w in WORD_RE.findall(line.lower()):
                freq[w] = freq.get(w, 0) + 1
    return freq


def write_word_count(output_file: str, freq: dict[str, int]) -> None:
    # sorted: giảm dần theo count, rồi tăng dần theo từ
    items = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    with open(output_file, "w", encoding="utf-8") as f:
        for w, c in items:
            f.write(f"{w}\t{c}\n")


def bai_5() -> None:
    input_file = input("Nhập file văn bản cần đếm từ: ").strip()
    if not input_file:
        print("Bạn chưa nhập file.")
        return
    output_file = input("Nhập file output (mặc định word_count.txt): ").strip() or "word_count.txt"
    try:
        freq = word_frequency_from_file(input_file)
        write_word_count(output_file, freq)
        print(f"Đã ghi kết quả ra: {output_file}")
    except FileNotFoundError:
        print("Không tìm thấy file input.")
    except Exception as e:
        print("Lỗi:", e)


def main() -> None:
    while True:
        print("\n===== BT TUẦN 4 =====")
        print("1) Đọc data.txt: tổng/tb/max/min")
        print("2) Todo List (todos.json)")
        print("3) Đếm tần suất từ trong list từ")
        print("4) StudentManager (JSON)")
        print("5) Word frequency từ file -> word_count.txt")
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


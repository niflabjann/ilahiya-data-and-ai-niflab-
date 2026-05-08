class StudentMarks:
    def __init__(self, name: str) -> None:
        self.name = name
        self.marks = []  # list[int]

    def add_mark(self, mark: int) -> None:
        self.marks.append(mark)

    def total(self) -> int:
        return sum(self.marks)

    def percentage(self) -> float:
        if len(self.marks) == 0:
            return 0.0
        return (self.total() / (len(self.marks) * 100)) * 100


def read_marks(count: int) -> list[int]:
    result = []
    for i in range(count):
        mark = int(input(f"Enter mark {i + 1} (0-100): ").strip())
        result.append(mark)
    return result


def print_result(student: StudentMarks) -> None:
    print("\nResult")
    print("Name:", student.name)
    print("Marks:", student.marks)
    print("Total:", student.total())
    print("Percentage:", round(student.percentage(), 2), "%")


name = input("Enter student name: ").strip()
student = StudentMarks(name)

marks_list = read_marks(3)
for m in marks_list:
    student.add_mark(m)

print_result(student)


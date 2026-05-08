class Student:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> None:
        print("Hi", self.name)


s1 = Student("Ali")
s1.greet()


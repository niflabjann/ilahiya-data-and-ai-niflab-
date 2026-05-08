def greet(name: str) -> None:
    print("Hi", name)


def add(a: int, b: int) -> int:
    return a + b


def say_hello() -> None:
    print("Hello!")


def square(n: int) -> int:
    return n * n


def power(base: int, exponent: int = 2) -> int:
    return base**exponent


def full_name(first: str, last: str, *, title: str = "") -> str:
    if title:
        return f"{title} {first} {last}"
    return f"{first} {last}"


def total_sum(*numbers: int) -> int:
    total = 0
    for n in numbers:
        total += n
    return total


def print_profile(**info: str) -> None:
    for key, value in info.items():
        print(f"{key} = {value}")


def is_even(n: int) -> bool:
    return n % 2 == 0


multiply = lambda a, b: a * b  # small one-line function


print("1) No-argument function")
say_hello()

print("\n2) Function with parameter")
greet("Ali")

print("\n3) Function with return value")
result = add(2, 3)
print("2 + 3 =", result)

print("\n4) Another return example")
print("square(6) =", square(6))

print("\n5) Default parameter (exponent defaults to 2)")
print("power(5) =", power(5))
print("power(5, 3) =", power(5, 3))

print("\n6) Keyword-only argument (title must be named)")
print(full_name("Sara", "Khan"))
print(full_name("Sara", "Khan", title="Ms."))

print("\n7) *args (any number of values)")
print("total_sum(1, 2, 3) =", total_sum(1, 2, 3))
print("total_sum(10, 20, 30, 40) =", total_sum(10, 20, 30, 40))

print("\n8) **kwargs (named info as key=value)")
print_profile(name="Hamza", city="Karachi", course="Python")

print("\n9) Function returning True/False")
print("is_even(10) =", is_even(10))
print("is_even(11) =", is_even(11))

print("\n10) Lambda function")
print("multiply(4, 5) =", multiply(4, 5))

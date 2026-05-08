from __future__ import annotations

print("Python note: Python does NOT support classic function overloading")
print("But we can achieve similar behavior using patterns like these.\n")


print("1) Overloading-like behavior using default parameters")


def greet(name: str, times: int = 1) -> None:
    for _ in range(times):
        print("Hello", name)


greet("Ali")
greet("Ali", 3)


print("\n2) Overloading-like behavior using *args (different number of inputs)")


def add(*nums: int) -> int:
    total = 0
    for n in nums:
        total += n
    return total


print("add(2, 3) =", add(2, 3))
print("add(1, 2, 3, 4) =", add(1, 2, 3, 4))

print("Example 1) Simple if/else (string check)")
is_raining = "yes"  # try: "no"
if is_raining == "yes":
    print("Take an umbrella.")
else:
    print("No umbrella needed.")

print("\nExample 2) if / elif / else (grade check)")
marks = 76
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

print("\nExample 3) Number checking (positive / negative / zero)")
num = -5
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is zero")

print("\nExample 4) Number checking (even / odd)")
n = 11
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")

print("\nExample 5) Multiple conditions using and/or")
age = 20
has_id = True
if age >= 18 and has_id:
    print("Allowed (18+ and has ID).")
else:
    print("Not allowed.")

day = "saturday"
if day == "saturday" or day == "sunday":
    print("Weekend")
else:
    print("Weekday")

print("\nExample 6) Nested if (divisibility checks)")
x = 30
if x % 5 == 0:
    if x % 3 == 0:
        print(x, "is divisible by 5 and 3")
    else:
        print(x, "is divisible by 5 but not by 3")
else:
    print(x, "is not divisible by 5")

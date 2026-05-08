names = ["Ali", "Sara", "Hamza"]

print("1) Looping over a list")
for name in names:
    print("Hi", name)

print("\n2) Looping over a string (each character)")
word = "Python"
for ch in word:
    print(ch)

print("\n3) range() loop (0..4)")
for i in range(5):
    print("i =", i)

print("\n4) range() with start, stop, step (2..10 step 2)")
for i in range(2, 11, 2):
    print("even =", i)

print("\n5) enumerate() to get index + value")
for index, name in enumerate(names, start=1):
    print(index, "=>", name)

print("\n6) Looping over a dictionary (keys / values / items)")
marks = {"Ali": 90, "Sara": 95, "Hamza": 88}
print("keys:")
for k in marks:
    print(k)
print("values:")
for v in marks.values():
    print(v)
print("items:")
for student, score in marks.items():
    print(student, "scored", score)

print("\n7) Nested loop (small multiplication table)")
for a in range(1, 4):
    for b in range(1, 4):
        print(a * b, end=" ")
    print()

print("\n8) break and continue")
for n in range(1, 8):
    if n == 3:
        continue  # skip 3
    if n == 6:
        break  # stop at 6
    print("n =", n)

print("\n9) for...else (else runs only if loop did NOT break)")
for n in range(1, 5):
    if n == 10:
        print("Found 10")
        break
else:
    print("10 not found")

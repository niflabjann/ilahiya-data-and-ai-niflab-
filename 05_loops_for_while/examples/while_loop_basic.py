print("1) Counter-controlled while loop")
count = 1
while count <= 3:
    print("Count =", count)
    count += 1

print("\n2) Sentinel-style loop (simulated input list)")
inputs = ["10", "5", "stop", "99"]  # after "stop" we should stop processing
i = 0
while i < len(inputs) and inputs[i] != "stop":
    print("Got:", inputs[i])
    i += 1

print("\n3) Infinite loop pattern with break/continue")
n = 0
while True:
    n += 1
    if n == 2:
        continue  # skip printing 2
    if n == 5:
        break  # stop the loop
    print("n =", n)

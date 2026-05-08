with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Ali,tea,2\n")
    f.write("Sara,coffee,1\n")

with open("sample.txt", "r", encoding="utf-8") as f:
    data = f.read()

print(data)


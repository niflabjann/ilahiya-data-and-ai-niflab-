from utils import is_valid_item, normalize_item

print("Welcome to the Vending Machine (Imports Demo)")
name = input("Enter your name: ").strip()
item = normalize_item(input("What do you want? (tea/coffee): "))

if is_valid_item(item):
    print(f"Hi {name}, your {item} is ready.")
else:
    print(f"Sorry {name}, we only serve tea or coffee.")


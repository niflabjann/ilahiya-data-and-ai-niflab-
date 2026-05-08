print("Welcome to the Vending Machine")

name = input("Enter your name: ").strip()
item = input("What do you want? (tea/coffee): ").strip().lower()

if item == "tea":
    print("Hi", name + ", your tea is ready.")
elif item == "coffee":
    print("Hi", name + ", your coffee is ready.")
else:
    print("Sorry", name + ", we only serve tea or coffee.")


print("Welcome to the Vending Machine")

name = input("Enter your name: ").strip()
item = input("What do you want? (tea/coffee): ").strip().lower()

if item != "tea" and item != "coffee":
    print("Sorry", name + ", we only serve tea or coffee.")
else:
    qty_text = input("How many cups do you want?: ").strip()
    qty = int(qty_text)

    for i in range(qty):
        print("Order", i + 1, "for", name + ":", item, "is ready.")


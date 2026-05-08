text = input("Enter a number: ").strip()

try:
    value = int(text)
    print("You entered:", value)
except ValueError:
    print("That was not a valid integer.")


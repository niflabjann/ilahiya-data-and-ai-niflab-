from vending_machine.core import Order, VendingMachine


def _normalize(text: str) -> str:
    return text.strip().lower()


def _read_positive_int(prompt: str) -> int:
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if value <= 0:
            print("Please enter a number greater than 0.")
            continue
        return value


def _print_menu(vm: VendingMachine) -> None:
    print("\nMenu:")
    for item, price in vm.menu.items():
        print(f"- {item} (Rs {price}) | stock: {vm.stock[item]}")


def run() -> None:
    vm = VendingMachine()

    print("Welcome to the Vending Machine")
    name = input("Enter your name: ").strip()

    while True:
        _print_menu(vm)
        item = _normalize(input("\nChoose item (tea/coffee) or 'exit': "))
        if item == "exit":
            print("Thank you. Goodbye!")
            break

        if not vm.is_valid_item(item):
            print("Invalid item. Please choose tea or coffee.")
            continue

        qty = _read_positive_int("Enter quantity: ")

        if not vm.can_serve(item, qty):
            print("Sorry, not enough stock.")
            continue

        order = Order(name=name, item=item, qty=qty)
        total = vm.serve(order)

        for i in range(order.qty):
            print(f"Order {i + 1} for {order.name}: {order.item} is ready.")

        print(f"Total bill: Rs {total}")


from dataclasses import dataclass


@dataclass
class Order:
    name: str
    item: str
    qty: int


class VendingMachine:
    def __init__(self) -> None:
        self.menu = {"tea": 20, "coffee": 30}
        self.stock = {"tea": 10, "coffee": 10}

    def is_valid_item(self, item: str) -> bool:
        return item in self.menu

    def can_serve(self, item: str, qty: int) -> bool:
        return self.is_valid_item(item) and qty > 0 and self.stock.get(item, 0) >= qty

    def total_price(self, item: str, qty: int) -> int:
        return self.menu[item] * qty

    def serve(self, order: Order) -> int:
        if not self.can_serve(order.item, order.qty):
            raise ValueError("Cannot serve this order")
        self.stock[order.item] -= order.qty
        return self.total_price(order.item, order.qty)


from dataclasses import dataclass, field
from enum import Enum, auto


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


@dataclass
class LineItem:
    item: str
    quantity: int
    price: int

    def total_price(self) -> int:
        return self.quantity * self.price


@dataclass
class Order:
    lineitems: list[LineItem] = field(default_factory=list)
    status: PaymentStatus = PaymentStatus.OPEN

    def add_item(self, item: LineItem) -> None:
        self.lineitems.append(item)

    @property
    def total_price(self) -> int:
        return sum(item.total_price() for item in self.lineitems)


def main() -> None:
    order = Order()
    order.add_item(LineItem("Keyboard", 1, 5000))
    order.add_item(LineItem("SSD", 1, 15000))
    order.add_item(LineItem("USB cable", 2, 500))

    print(f"The total price is: ${(order.total_price / 100):.2f}.")


if __name__ == "__main__":
    main()

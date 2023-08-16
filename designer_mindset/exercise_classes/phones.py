from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Address:
    street: str
    postal_code: str
    city: str


@dataclass
class Customer:
    name: str
    email: str
    addresses: list[Address] = field(default_factory=list)


@dataclass
class Phone:
    brand: str
    model: str
    price: float
    serial_number: int


@dataclass
class Plan:
    customer: Customer
    phone: Phone
    start_date: datetime
    months: int
    monthly_price: float
    is_phone_included: bool


def main():
    address = Address("Batcase 69", "8069", "Gotham")
    customer = Customer("Bruce", address, "bat@man.com")
    phone = Phone("Nokia", "3310", 99.99, 987345)
    plan = Plan(customer, phone, datetime.now(), 12, 9.99, True)
    print(address)
    print(customer)
    print(phone)
    print(plan)


if __name__ == "__main__":
    main()

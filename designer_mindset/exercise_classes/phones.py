from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Customer:
    name: str
    address: str
    email: str


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
    customer = Customer("Bruce", "Batcave 69", "bat@man.com")
    phone = Phone("Nokia", "3310", 99.99, 987345)
    plan = Plan(customer, phone, datetime.now(), 12, 9.99, True)
    print(customer)
    print(phone)
    print(plan)


if __name__ == "__main__":
    main()

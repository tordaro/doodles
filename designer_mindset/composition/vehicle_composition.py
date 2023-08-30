from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Protocol


class Pricing(Protocol):
    def get_total_price(self) -> int:
        ...


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


@dataclass
class PricePerDay:
    num_days: int
    price_per_day: int

    def get_total_price(self) -> int:
        return self.price_per_day * self.num_days


@dataclass
class PricePerMonth:
    num_months: int
    price_per_month: int

    def get_total_price(self) -> int:
        return self.price_per_month * self.num_months


@dataclass
class PricePerKm:
    num_km: int
    price_per_km: int

    def get_total_price(self) -> int:
        return self.price_per_km * self.num_km


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool = False
    pricing: list[Pricing] = field(default_factory=list)


@dataclass
class Car(Vehicle):
    number_of_seats: int = 5
    storage_capacity_litres: int = 300


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle = TruckCabStyle.REGULAR


@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    price_per_month: int
    reserved: bool


def main():
    # Example of a car that you can rent per day
    price_per_day = PricePerDay(price_per_day=50, num_days=1)
    price_per_month = PricePerMonth(price_per_month=1000, num_months=1)
    price_per_km = PricePerKm(price_per_km=10, num_km=100)
    ford = Car(
        brand="Ford",
        model="Fiesta",
        color="red",
        fuel_type=FuelType.PETROL,
        license_plate="ABC-123",
        reserved=False,
        pricing=[price_per_km, price_per_day, price_per_month],
        number_of_seats=5,
        storage_capacity_litres=300,
    )
    print(ford)
    # Example of a car that you can rent per month
    tesla = Car(
        brand="Tesla",
        model="Model 3",
        color="black",
        fuel_type=FuelType.ELECTRIC,
        license_plate="DEF-456",
        reserved=False,
        pricing=[price_per_km, price_per_day, price_per_month],
        number_of_seats=5,
        storage_capacity_litres=300,
    )
    print(tesla)


if __name__ == "__main__":
    main()

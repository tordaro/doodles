from dataclasses import dataclass
from typing import Iterable


@dataclass
class VehicleData:
    """A class to hold vehicle data."""

    brand: str
    price_per_day: int
    price_per_km: int
    km_free_limit: int = 100

    def compute_rental_cost(self, days: int, km: int) -> int:
        """Computes the rental cost for a vehicle."""
        paid_kms = max(km - self.km_free_limit, 0)
        return self.price_per_km * paid_kms + self.price_per_day * days


def read_vehicle_type(vehicle_data: Iterable[str]) -> str:
    """Reads the vehicle type from the user."""
    vehicle_type = ""
    while vehicle_type not in vehicle_data:
        vehicle_type = input(f"What type of vehicle would you like to rent ({', '.join(vehicle_data)})? ")
    return vehicle_type


def read_rent_days() -> int:
    """Reads the number of days from the user."""
    days = 0
    while days < 1:
        days_str = input("How many days would you like to rent the vehicle? (enter a positive number) ")
        try:
            days = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return days


def read_kms_to_drive() -> int:
    """Reads the number of kilometers to drive from the user."""
    km = 0
    while km < 1:
        km_str = input("How many kilometers would you like to drive (enter a positive number)? ")
        try:
            km = int(km_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return km


def main():
    vehicle_data = {
        "vw": VehicleData(brand="vw", price_per_km=30, price_per_day=6000),
        "bmw": VehicleData(brand="bmw", price_per_km=35, price_per_day=8500),
        "ford": VehicleData(brand="ford", price_per_km=25, price_per_day=12000),
    }

    vehicle_type = read_vehicle_type(vehicle_data.keys())
    days = read_rent_days()
    km = read_kms_to_drive()

    vehicle = vehicle_data[vehicle_type]
    rental_price = vehicle.compute_rental_cost(days, km)

    print(f"The total price of the rental is ${(rental_price / 100):.2f}")


if __name__ == "__main__":
    main()

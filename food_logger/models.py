from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class Nutrition:
    # TODO: Use relative nutritional values
    protein: float
    carb: float
    fat: float
    calories: float = 0

    def calculate_calories(self) -> float:
        return self.protein * 4 + self.carb * 4 + self.fat * 9

    def __post_init__(self):
        self.calories = self.calories if self.calories else self.calculate_calories()

    def __add__(self, other: "Nutrition") -> "Nutrition":
        nutrition = Nutrition(
            self.protein + other.protein,
            self.carb + other.carb,
            self.fat + other.fat,
            self.calories + other.calories,
        )
        return nutrition

    def __str__(self):
        energy = f"Energy [kcal]: {self.calories:>4.0f};"
        protein = f"Proteins [g]: {self.protein:>4.0f};"
        carb = f"Carbohydrates [g] {self.carb:>4.0f};"
        fat = f"Fats [g]: {self.fat:>4.0f}"
        return f"{energy:>20}{carb:>30}{protein:>20}{fat:>20}"


class FoodComponent(ABC):
    @abstractmethod
    def add(self, component: "FoodComponent") -> None:
        pass

    @abstractmethod
    def remove(self, component: "FoodComponent") -> None:
        pass

    @abstractmethod
    def get_nutrition(self) -> Nutrition:
        pass

    @abstractmethod
    def get_mass(self) -> float:
        pass


@dataclass
class Ingredient(FoodComponent):
    name: str
    nutrition: Nutrition
    mass_g: float  # mass in grams

    def add(self, component: "FoodComponent") -> None:
        raise ValueError("Cannot add to an Ingredient")

    def remove(self, component: "FoodComponent") -> None:
        raise ValueError("Cannot remove from an Ingredient")

    def get_nutrition(self) -> Nutrition:
        return self.nutrition

    def get_mass(self) -> float:
        return self.mass_g

    def __str__(self) -> str:
        header = f"{self.name} ({self.mass_g:.0f} g):"
        return f"{header:<30}{self.nutrition}"


@dataclass
class Meal(FoodComponent):
    name: str
    components: list[FoodComponent] = field(default_factory=list)

    def add(self, component: "FoodComponent") -> None:
        self.components.append(component)

    def remove(self, component: "FoodComponent") -> None:
        self.components.remove(component)

    def get_nutrition(self) -> Nutrition:
        total_nutrition = Nutrition(0, 0, 0, 0)
        for component in self.components:
            total_nutrition += component.get_nutrition()
        return total_nutrition

    def get_mass(self) -> float:
        return sum([component.get_mass() for component in self.components])

    def __str__(self) -> str:
        components_str = "\n".join([f"  {str(component)}" for component in self.components])
        header = f"{self.name} ({self.get_mass()} g):"
        return f"{header:<30}" + f"{self.get_nutrition()} kcal\n" + f"{components_str}"


def main():
    rice = Ingredient("Rice", Nutrition(4.3, 44.5, 0.4), 80)
    chicken = Ingredient("Chicken", Nutrition(25, 0, 20), 200)

    chicken_rice_bowl = Meal("Chicken Rice Bowl")
    chicken_rice_bowl.add(rice)
    chicken_rice_bowl.add(chicken)

    print(str(chicken_rice_bowl))


if __name__ == "__main__":
    main()

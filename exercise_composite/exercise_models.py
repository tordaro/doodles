from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any
import numexpr as ne


class Composite(ABC):
    @abstractmethod
    def add(self, component: "Composite") -> None:
        pass

    @abstractmethod
    def remove(self, component: "Composite") -> None:
        pass

    @abstractmethod
    def get_equipment(self) -> set[str]:
        pass

    @abstractmethod
    def get_dependencies(self) -> dict[str, type]:
        pass


@dataclass
class Movement(Composite):
    name: str
    work_formula: str
    dependencies: dict[str, type]
    equipment: set[str] = field(default_factory=set)

    def add(self, component: "Composite") -> None:
        raise ValueError("Cannot add to a Movement.")

    def remove(self, component: "Composite") -> None:
        raise ValueError("Cannot remove from a Movement.")

    def get_equipment(self) -> set[str]:
        return self.equipment

    def get_dependencies(self) -> dict[str, type]:
        return self.dependencies


@dataclass
class Exercise(Composite):
    name: str
    components: list[Composite] = field(default_factory=list)

    def add(self, component: "Composite") -> None:
        self.components.append(component)

    def remove(self, component: "Composite") -> None:
        self.components.remove(component)

    def get_equipment(self) -> set[str]:
        all_equipment: set[str] = set()
        for component in self.components:
            all_equipment.update(component.get_equipment())
        return all_equipment

    def get_dependencies(self) -> dict[str, type]:
        all_dependencies = dict()
        for component in self.components:
            all_dependencies.update(component.get_dependencies())
        return all_dependencies


def main():
    deadlift = Movement(
        name="Deadlift",
        work_formula="a * b + 4",
        dependencies={"a": float, "b": float},
        equipment={"Barbell", "Locks"},
    )
    front_squat = Movement(
        name="Front squat", work_formula="b + c", dependencies={"b": float, "c": float}, equipment={"Barbell", "Shoes"}
    )
    clean = Exercise("Clean")
    clean.add(deadlift)
    clean.add(front_squat)

    jerk = Movement(
        name="Jerk",
        work_formula="height * width",
        dependencies={"height": float, "width": float},
        equipment={"Barbell", "Belt"},
    )
    clean_jerk = Exercise("Clean & Jerk")
    clean_jerk.add(clean)
    clean_jerk.add(jerk)
    print(clean_jerk)
    print(clean_jerk.get_equipment())
    print(clean_jerk.get_dependencies())


if __name__ == "__main__":
    main()

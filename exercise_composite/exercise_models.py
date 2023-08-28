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
    def get_dependencies(self) -> dict[str, str]:
        pass

    @abstractmethod
    def calculate_work(self, dependencies: dict[str, float]) -> float:
        pass


@dataclass
class Movement(Composite):
    name: str
    work_formula: str
    dependencies: dict[str, str]
    equipment: set[str] = field(default_factory=set)

    def add(self, component: "Composite") -> None:
        raise ValueError("Cannot add to a Movement.")

    def remove(self, component: "Composite") -> None:
        raise ValueError("Cannot remove from a Movement.")

    def get_equipment(self) -> set[str]:
        return self.equipment

    def get_dependencies(self) -> dict[str, str]:
        # TODO: Implement validation function that ensures that the dependencies match the work formula
        return self.dependencies

    def calculate_work(self, dependencies: dict[str, float]) -> float:
        kcal = 4184.0
        constants = {"g": 9.80665}
        local_dict = {**dependencies, **constants}
        work = float(ne.evaluate(self.work_formula, local_dict=local_dict, global_dict={})) / kcal
        return work


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

    def get_dependencies(self) -> dict[str, str]:
        all_dependencies = dict()
        for component in self.components:
            all_dependencies.update(component.get_dependencies())
        return all_dependencies

    def calculate_work(self, dependencies: dict[str, float]) -> float:
        work = 0.0
        for component in self.components:
            work += component.calculate_work(dependencies)
        return work


def main():
    clean = Movement(
        name="Clean",
        work_formula="(leg_length + trunk_length) * mass * g",
        dependencies={"leg_length": "Length of legs", "trunk_length": "Length of trunk", "mass": "Total mass"},
        equipment={"Barbell", "Shoes"},
    )

    jerk = Movement(
        name="Jerk",
        work_formula="arm_length * mass * g",
        dependencies={"arm_length": "Total length of one arm", "mass": "Total mass"},
        equipment={"Barbell", "Belt"},
    )
    clean_jerk = Exercise("Clean & Jerk")
    clean_jerk.add(clean)
    clean_jerk.add(jerk)
    dependencies = {"leg_length": 0.9, "trunk_length": 0.6, "mass": 80, "arm_length": 0.25 + 0.28}
    print(clean_jerk)
    print(clean_jerk.get_dependencies())

    print(f"\n{clean_jerk.name}: ")
    print("Needed equipment: ", " ,".join(clean_jerk.get_equipment()))
    print(f"{clean_jerk.calculate_work(dependencies):.2f} kcal per rep")


if __name__ == "__main__":
    main()

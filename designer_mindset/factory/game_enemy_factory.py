from dataclasses import dataclass
from enum import StrEnum
from abc import ABC, abstractmethod
import random


class EnemyType(StrEnum):
    KNIGHT = "knight"
    ARCHER = "archer"
    WIZARD = "wizard"


@dataclass
class Enemy:
    enemy_type: EnemyType
    health: int
    attack_power: int
    defense: int


class EnemyFactory(ABC):
    @abstractmethod
    def spawn(self) -> Enemy:
        pass


class EasyEnemyFactory(EnemyFactory):
    def spawn(self) -> Enemy:
        enemy_type = random.choice([EnemyType.ARCHER, EnemyType.WIZARD, EnemyType.KNIGHT])
        health = random.randint(1, 30)
        attack_power = random.randint(1, 30)
        defence = random.randint(1, 30)
        return Enemy(enemy_type, health, attack_power, defence)


class MediumEnemyFactory(EnemyFactory):
    def spawn(self) -> Enemy:
        enemy_type = random.choice([EnemyType.ARCHER, EnemyType.WIZARD, EnemyType.KNIGHT])
        health = random.randint(30, 60)
        attack_power = random.randint(30, 60)
        defence = random.randint(30, 60)
        return Enemy(enemy_type, health, attack_power, defence)


class HardEnemyFactory(EnemyFactory):
    def spawn(self) -> Enemy:
        enemy_type = random.choice([EnemyType.ARCHER, EnemyType.WIZARD, EnemyType.KNIGHT])
        health = random.randint(60, 90)
        attack_power = random.randint(60, 90)
        defence = random.randint(60, 90)
        return Enemy(enemy_type, health, attack_power, defence)


def main() -> None:
    easy_factory = EasyEnemyFactory()
    for _ in range(5):
        enemy = easy_factory.spawn()
        print(enemy)

    medium_factory = MediumEnemyFactory()
    for _ in range(5):
        enemy = medium_factory.spawn()
        print(enemy)

    hard_factory = HardEnemyFactory()
    for _ in range(5):
        enemy = hard_factory.spawn()
        print(enemy)


if __name__ == "__main__":
    main()

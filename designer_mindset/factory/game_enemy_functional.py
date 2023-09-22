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


def easy_spawn() -> Enemy:
    enemy_type = random.choice([EnemyType.ARCHER, EnemyType.WIZARD, EnemyType.KNIGHT])
    health = random.randint(1, 30)
    attack_power = random.randint(1, 30)
    defence = random.randint(1, 30)
    return Enemy(enemy_type, health, attack_power, defence)


def medium_spawn() -> Enemy:
    enemy_type = random.choice([EnemyType.ARCHER, EnemyType.WIZARD, EnemyType.KNIGHT])
    health = random.randint(30, 60)
    attack_power = random.randint(30, 60)
    defence = random.randint(30, 60)
    return Enemy(enemy_type, health, attack_power, defence)


def hard_spawn() -> Enemy:
    enemy_type = random.choice([EnemyType.ARCHER, EnemyType.WIZARD, EnemyType.KNIGHT])
    health = random.randint(60, 90)
    attack_power = random.randint(60, 90)
    defence = random.randint(60, 90)
    return Enemy(enemy_type, health, attack_power, defence)


def main() -> None:
    for _ in range(5):
        enemy = easy_spawn()
        print(enemy)

    for _ in range(5):
        enemy = medium_spawn()
        print(enemy)

    for _ in range(5):
        enemy = hard_spawn()
        print(enemy)


if __name__ == "__main__":
    main()

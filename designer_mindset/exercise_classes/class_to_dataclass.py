from dataclasses import dataclass, field


@dataclass
class A:
    _length: int = field(init=False, default=0)


@dataclass(slots=True)
class B:
    x: int
    y: str = "hello"
    l: list[int] = field(default_factory=list)


@dataclass
class C:
    a: int = 3
    b: int = field(init=False)

    def __post_init__(self) -> None:
        self.b = self.a + 3


def main():
    a = A()
    print(a._length)

    b1 = B(5, "batman", [2, 3, 4])
    print(b1.x, b1.y, b1.l)
    b2 = B(x=1)
    print(b2.x, b2.y, b2.l)

    c = C(4)
    print(c.a, c.b)


if __name__ == "__main__":
    main()

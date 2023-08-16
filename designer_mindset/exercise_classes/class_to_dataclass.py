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
    print(a)

    b1 = B(5, "batman", [2, 3, 4])
    print(b1)
    b2 = B(x=1)
    print(b2)

    c = C(4)
    print(c)


if __name__ == "__main__":
    main()

import random
import string
from functools import partial
from datetime import datetime
from typing import Callable

SelectFn = Callable[[], str]


def generate_id(length: int, select_fn: SelectFn) -> str:
    return "".join(select_fn() for _ in range(length))


def weekday(date: datetime) -> str:
    return f"{date:%A}"


def main() -> None:
    select_fn = partial(random.choice, seq=string.ascii_letters + string.digits)
    my_id = generate_id(10, select_fn)  # type: ignore

    my_date = datetime.now()
    today = weekday(my_date)

    print(f"Today is {today}")
    print(f"Your id = {my_id}")


if __name__ == "__main__":
    main()

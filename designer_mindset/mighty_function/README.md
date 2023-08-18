## 1. Pure functions and side effects

Consider the following Python program:

```python
import random
import string
from datetime import datetime

def generate_id(length: int) -> str:
  return "".join(
    random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
  )

def weekday() -> str:
  today = datetime.today()
  return f"{today:%A}"

def main() -> None:
  print(f"Today is a {weekday()}")
  print(f"Your id = {generate_id(10)}")

if __name__ == "__main__":
  main()
```

a) Both generate_id and weekday are not pure functions. Why not? How would you write tests for these functions?

b) Rewrite both functions so that they are pure functions. Observe what happens to the main function after making this change. Are the functions now easier to test? Are they easier to use as well?

## 2. Classes or functions

Consider the following class:

```python
@dataclass
class Laptop:
 machine_name: str = "DULL"

 def install_os(self) -> None:
  print("Installing OS")

 def format_hd(self) -> None:
  print("Formatting the hard drive")

 def create_admin_user(self, password: str) -> None:
  print(f"Creating admin user with password {password}.")
```

We want to add the capability to the software to reset the laptop to the factory settings. This involves the following steps:

    Format the hard drive.
    Make sure the machine name is set to "DULL", which is the name of the company that produced the laptop.
    Install the os.
    Create an admin user with password "admin"

a) Extend the program with this capability relying on object-oriented programming.

b) Write another version of the same program, but this time, don't extend the class with new capabilities, use a separate function instead. How would you describe the differences between the two versions?
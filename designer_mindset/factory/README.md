# Exercises
## QR Codes
Consider the following program that uses a device's camera to scan a QR code and then navigates to the URL represented by the QR code on the device's browser:

```python
class Camera(StrEnum):
  FRONT = "front"
  BACK = "back"

@dataclass
class QRScanner:
  camera: Camera = Camera.FRONT

  def choose_camera(self, camera: Camera) -> None:
    print(f"Choosing camera {camera.value}.")
    self.camera = camera

  def scan(self) -> str:
    print(f"Scanning QR code with {self.camera.value} camera.")
    return "https://www.arjancodes.com"

class Browser:
  def open(self, url: str) -> None:
    print(f"Opening {url} in the browser.")

  def open_from_qr_code(self) -> None:
    qr = QRScanner()
    qr.choose_camera(Camera.BACK)
    url = qr.scan()
    self.open(url)

def main() -> None:
  print("Navigating to website on device.")
  browser = Browser()
  browser.open_from_qr_code()
```

Apply the "Separate Creation From Use" principle to refactor this code.

## Game Enemy Factory
Suppose you're building a game that involves creating different types of enemies such as knights, wizards, and archers. Each enemy has different attributes such as health, attack power, and defense. Here's an example of an Enemy class:

```python
from dataclasses import dataclass
from enum import StrEnum

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
```
Your game also has "spawn points" that spawn new enemies. There are three types of spawn points:
- Easy spawn points spawn enemies with low health, low attack power, and low defense. Easy spawn points only spawn knights and archers.
- Medium spawn points spawn enemies with medium health, medium attack power, and medium defense. Medium spawn points spawn knights, wizards, and archers.
- Hard spawn points spawn enemies with high health, high attack power, and high defense. Hard spawn points only spawn wizards.

a) Create a Python application that uses the Abstract Factory pattern to create enemies based on the type of spawn point (easy, medium, or hard). The application should print the attributes of the enemies that are created.

b) What would be a more functional way to create enemies based on the type of spawn point? Update your application to use this approach.

Note: these two exercises use StrEnum, which is a type only supported by Python 3.11 and newer.
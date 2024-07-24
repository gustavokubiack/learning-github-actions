from dataclasses import dataclass
from typing import Any


@dataclass
class Calculator:
    x: int
    y: int

    def addition(self) -> int:
        return self.x + self.y

    def subtraction(self) -> int:
        return self.x - self.y

    def multiplication(self) -> float:
        return self.x * self.y

    def division(self) -> float:
        return self.x / self.y    
    
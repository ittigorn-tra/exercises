import math
import numbers
from abc import ABC, abstractmethod


class TwoDimensionShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(TwoDimensionShape):
    def __init__(self, radius: float) -> None:
        if (not isinstance(radius, numbers.Number)) or (radius <= 0):
            raise ValueError('The variable "radius" should be a positive number')

        self.radius = radius
        self.diameter = radius * 2

    def area(self) -> float:
        return math.pi * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    radius = 5.0
    c = Circle(radius)

    print('Radius'.ljust(10), ':', c.radius)
    print('Diameter'.ljust(10), ':', c.diameter)
    print('Area'.ljust(10), ':', c.area())
    print('Perimeter'.ljust(10), ':', c.perimeter())

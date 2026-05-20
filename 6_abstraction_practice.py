# ============================================
#   ABSTRACTION — Abstract Classes (ABC)
#   By: Mustafa Javed
# ============================================

# Abstract class = blueprint (cannot create its object directly)
# Every child class MUST implement the abstract method

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass    # child must define this


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# ── Test ──
c = Circle(6)
r = Rectangle(5, 7)
t = Triangle(4, 8)

print(f"Circle Area    : {c.area():.2f}")
print(f"Rectangle Area : {r.area()}")
print(f"Triangle Area  : {t.area()}")

# shape = Shape()    Error! Cannot create object of abstract class

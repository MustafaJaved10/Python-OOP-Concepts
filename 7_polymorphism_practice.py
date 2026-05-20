# ============================================
#   POLYMORPHISM & METHOD OVERRIDING
#   By: Mustafa Javed
# ============================================

# Polymorphism = same method name, different behavior
# Method Overriding = child changes parent's method


# ── 1. Basic Override ─────────────────────────
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")

a = Animal()
a.sound()

b = Dog()
b.sound()


# ── 2. Polymorphism — Loop through objects ────
class Cat:
    def sound(self):
        return "Meow~ (sweet voice)"

class DogP:
    def sound(self):
        return "Bark! (loud voice)"

for animal in (Cat(), DogP()):
    print(animal.sound())


# ── 3. Inheritance + Polymorphism ─────────────
class AnimalW:
    def weight(self):
        print("Weight: Heavy")

class Lion(AnimalW):
    def weight(self):
        print("Weight: Average")

class Leopard(AnimalW):
    def weight(self):
        print("Weight: Light")

for x in (AnimalW(), Lion(), Leopard()):
    x.weight()


# ── 4. Polymorphism with Constructor ──────────
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Moving...")

class FastCar(Vehicle):
    def move(self):
        print(f"{self.brand} moves FAST ")

class SlowCar(Vehicle):
    def move(self):
        print(f"{self.brand} moves slow ")

car1 = FastCar("Leopard")
car2 = SlowCar("Old Lion")
car3 = Vehicle("Generic")

for x in (car1, car2, car3):
    x.move()


# ── 5. Person + Student Polymorphism ──────────
class PersonP:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, Age is {self.age}")

class StudentP(PersonP):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):    # overrides parent method
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

p = PersonP("Mustafa", 20)
s = StudentP("Ali", 22, 180)

for x in (p, s):
    x.introduce()

# ============================================
#   INHERITANCE BASICS
#   By: Mustafa Javed
# ============================================

# Inheritance = child class gets all properties
#               and methods of parent class


# ── 1. Basic Inheritance (pass) ───────────────
class Hospital:
    def __init__(self, f, l):
        self.first = f
        self.last = l

    def info(self):
        print(self.first, self.last)

class Patient(Hospital):
    pass    # inherits everything from Hospital

x = Hospital("New", "Good")
x.info()


# ── 2. Inheritance with super() ───────────────
class Fruit:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def info(self):
        print(self.name, self.type_)

class Business(Fruit):
    def __init__(self, name, type_, rate):
        super().__init__(name, type_)   # call parent constructor
        self.rate = rate

a = Business("Fruits", "Fresh", 1000)
a.info()
print(a.rate)


# ── 3. Inheritance — Graduation Year Example ──
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def prnt(self):
        print(f"Name: {self.name}, Age: {self.age}")

class StudentGrad(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduation_year = year

x = StudentGrad("Mustafa", 19, 2028)
x.prnt()
print(f"Graduation Year: {x.graduation_year}")


# ── 4. Inheritance — Son & Father Example ─────
class Papa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Son's name: {self.name}, Age: {self.age}")

class Son(Papa):
    pass

x = Son("Saboor", 13)
x.display()

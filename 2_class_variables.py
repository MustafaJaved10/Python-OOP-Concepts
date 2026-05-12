# ============================================
#   CLASS VARIABLES vs INSTANCE VARIABLES
#   + @classmethod
#   By: Mustafa Javed
# ============================================


# ── 1. Class Variable vs Instance Variable ────
class Student:
    school = "UMT"          # class variable (shared by all)

    def __init__(self, name):
        self.name = name    # instance variable (unique per object)

s1 = Student("Mustafa")
s2 = Student("Ali")

print(s1.name, s1.school)
print(s2.name, s2.school)

Student.school = "LUMS"     # change for ALL objects
print(s1.school)


# ── 2. Class Variable in Car Example ─────────
class Car:
    company = "Toyota"

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def show_info(self):
        print(f"Company: {self.company}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

c = Car("Corolla", 2020)
c.show_info()

Car.company = "Honda"       # change company
c.show_info()


# ── 3. @classmethod ───────────────────────────
# self  → for instance variables  (object-specific)
# cls   → for class variables     (shared)

class Viral:
    value = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def increase_value(cls):
        cls.value += 1

    def show(self):
        print(f"Name: {self.name} | Value: {Viral.value}")

v1 = Viral("Mustafa")
v1.show()

Viral.increase_value()
v1.show()

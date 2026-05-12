# ============================================================
# OOP Python - Basics: Classes, Objects, Constructors
# ============================================================

# Q1: Basic class with default parameter
class Info:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Info("Mustafa", 19)
p2 = Info("Hamza")   # uses default age=18
print(p1.name, p1.age)
print(p2.name, p2.age)


# Q2: Class variable vs instance variable
class Me:
    quantity = "too much"    # class variable (shared)

    def __init__(self, name, age):
        self.name = name     # instance variable
        self.age = age

    def greet(self):
        print(f"Name: {self.name}, Age: {self.age}")

Me.quantity = "Too less"    # modifying class variable
p1 = Me("Mus", 19)
p1.greet()
print(p1.quantity)


# Q3: Instance with dynamic attributes
class InfoDetail:
    def __init__(self, name, age, length):
        self.name = name
        self.age = age
        self.length = length

    def display(self):
        self.age += 1
        self.length += 0.74
        print(f"Name: {self.name}, Age: {self.age}, Length: {self.length}")

p1 = InfoDetail("Mustafa", 20, 2.5)
p1.height = 5.5    # adding new property dynamically
p1.display()
p1.display()


# Q4: Getter and Setter methods
class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def get_age(self):
        return self.age

s = Car("Mustafa", 20)
print(s.get_name(), s.get_age())
s.set_name("Ali")
print(s.get_name())


# Q5: Class variable shared across all instances
class Student:
    school = "UMT"      # class variable

    def __init__(self, name):
        self.name = name    # instance variable

s1 = Student("Mustafa")
s2 = Student("Ali")
print(s1.name, s1.school)
print(s2.name, s2.school)

Student.school = "LUMS"   # change for all instances
print(s1.school)


# Q6: classmethod with @classmethod decorator
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

# ============================================
#   GETTERS & SETTERS
#   By: Mustafa Javed
# ============================================

# Getter  → reads  a value
# Setter  → updates a value


class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ── Setters ──
    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    # ── Getters ──
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


# Static usage
s = Car("Mustafa", 20)
print(s.get_name())
print(s.get_age())

s.set_name("Ali")
print(s.get_name())


# User input usage
name = input("Enter your name: ")
age = int(input("Enter your age: "))

s = Car(name, age)
print("Your name is:", s.get_name())
print("Your age is:", s.get_age())

if name == "Mustafa" and age == 20:
    print("Correct!")
else:
    print("Wrong!")

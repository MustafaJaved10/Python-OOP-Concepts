# ============================================
#   SCHOOL SYSTEM — Student & Teacher
#   Topic: Inheritance + isinstance()
#   By: Mustafa Javed
# ============================================


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show_info(self):
        super().show_info()
        print("Grade:", self.grade)

    def is_passed(self):
        return self.grade > 50   # True if passed


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        super().show_info()
        print("Subject:", self.subject)


# ── Create objects ──
s1 = Student("Ali", 20, 70)
s2 = Student("Hamza", 30, 40)
t1 = Teacher("Mustafa", 20, "Math")
t2 = Teacher("Khurram", 19, "Physics")

# ── Loop through all people ──
people = [s1, s2, t1, t2]

for p in people:
    p.show_info()
    if isinstance(p, Student):      # check if it's a Student
        print("Passed:", p.is_passed())
    print("-----------")

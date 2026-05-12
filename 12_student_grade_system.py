# ============================================
#   PROJECT: STUDENT GRADE SYSTEM
#   Topic: Classes, Methods, Logic
#   By: Mustafa Javed
# ============================================


class Student:
    def __init__(self, name, marks_list):
        self.name = name
        self.marks_list = marks_list

    def average(self):
        return sum(self.marks_list) / len(self.marks_list)

    def grade(self):
        avg = self.average()
        if avg > 90:
            return "A"
        elif avg > 70:
            return "B"
        elif avg > 50:
            return "C"
        else:
            return "F"

    def display(self):
        print(f"Name: {self.name} | Average: {self.average():.1f} | Grade: {self.grade()}")


# ── Test ──
s1 = Student("Mustafa", [100, 40, 70, 20])
s2 = Student("Ali",     [90, 95, 88, 92])
s3 = Student("Hamza",   [40, 35, 45, 50])

s1.display()
s2.display()
s3.display()

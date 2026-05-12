# ============================================
#   PROJECT: CAR SYSTEM
#   Topic: Classes, Methods, Conditions
#   By: Mustafa Javed
# ============================================


class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"Accelerated! Speed: {self.speed}")

    def brake(self):
        if self.speed - 10 < 0:
            self.speed = 0
        else:
            self.speed -= 10
        print(f"Braked! Speed: {self.speed}")

    def display(self):
        print(f"\nBrand: {self.brand} | Model: {self.model} | Speed: {self.speed}")


# ── Test ──
c = Car("Toyota", "Corolla 2025")
c.accelerate()
c.accelerate()
c.brake()
c.brake()
c.display()

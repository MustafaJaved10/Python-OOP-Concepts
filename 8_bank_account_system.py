# ============================================
#   BANK ACCOUNT SYSTEM
#   Topic: Inheritance + Method Overriding
#   By: Mustafa Javed
# ============================================


class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self._account_number = account_number   # protected
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} | New Balance: {self.balance}")
        else:
            print("Deposit must be greater than 0")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount} | New Balance: {self.balance}")
        else:
            print("Invalid amount or insufficient balance")

    def get_balance(self):
        return self.balance


# ── Student Account: gets bonus on every deposit ──
class StudentAccount(BankAccount):
    BONUS = 50  # student bonus per deposit

    def deposit(self, amount):
        super().deposit(amount)         # call parent deposit first
        self.balance += self.BONUS      # then add bonus
        print(f"🎓 Student Bonus Added: {self.BONUS} | Balance: {self.balance}")


# ── Test ──
s1 = StudentAccount(201, "Mustafa Javed", 1000)

s1.deposit(100)
s1.withdraw(300)

print("Final Balance:", s1.get_balance())

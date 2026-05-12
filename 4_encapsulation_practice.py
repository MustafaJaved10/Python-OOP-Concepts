# ============================================
#   ENCAPSULATION
#   Public / Protected / Private Members
#   By: Mustafa Javed
# ============================================

# public    → self.name       → accessible everywhere
# protected → self._name      → accessible in class & subclass
# private   → self.__name     → accessible only inside class


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._branch = "Lahore"     # protected
        self.__balance = balance    # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} | Balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount} | Balance: {self.__balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):      # getter for private variable
        return self.__balance


acc = BankAccount("Mustafa", 5000)

acc.deposit(1000)
acc.withdraw(500)
print("Balance:", acc.get_balance())

print("Owner:", acc.owner)          # public ✅
print("Branch:", acc._branch)       # protected ⚠️ (accessible but not recommended)
# print(acc.__balance)              # private ❌ will cause error

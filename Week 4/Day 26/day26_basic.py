# 📅 DAY 26 — INHERITANCE (Reuse & Extend Behavior)

# 🧠 PART 1: What Is Inheritance?
# Inheritance = child class uses parent class code
# Real-life example:
# Parent: Account
# Child: SavingsAccount
# Child: CurrentAccount
# They share common behavior but have special rules.

# 🧱 PART 2: Base (Parent) Class
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def show_balance(self):
        print("Balance:", self.balance)

# 👶 PART 3: Child Class (Inheritance Syntax)
class SavingsAccount(Account):
    pass
# Now SavingsAccount automatically has:
# deposit()
# show_balance()
# owner, balance

# 🔁 PART 4: Using Inherited Methods
acc = SavingsAccount("Raj", 1000)
acc.deposit(500)
acc.show_balance()
# ✔ No code duplication
# ✔ Clean reuse

# 🚀 PART 5: Extending Child Class
# Child class can add new behavior.
class SavingsAccount(Account):
    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest

# 🧠 PART 6: super() (VERY IMPORTANT)
# super() calls parent class methods.
class SavingsAccount(Account):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.rate = rate
# Why use super()?
# Avoid duplicate code
# Ensure parent setup runs correctly


# 🧠 Why ML Uses Inheritance
# Example (conceptual):
class Model:
    def train(self): pass
    def predict(self): pass
class LinearModel(Model):
    def train(self): ...

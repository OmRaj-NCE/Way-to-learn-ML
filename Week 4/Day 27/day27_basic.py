# 📅 DAY 27 — POLYMORPHISM (One Interface, Many Behaviors)

# 🧠 PART 1: What Is Polymorphism?
# Polymorphism = “many forms”
# Same method name
# Different behavior
# Depending on the object
# Real-life analogy:
# “Pay” using cash
# “Pay” using card
# “Pay” using UPI
# Same action → different implementation.

# 🧱 PART 2: Base Class with Common Method
class Account:
    def calculate_interest(self):
        print("Generic interest calculation")
# This defines the interface.

# 🔁 PART 3: Method Overriding (CORE)
# Child class redefines the same method.
class SavingsAccount(Account):
    def calculate_interest(self):
        print("Savings account interest calculated")
# Another child:
class FixedDeposit(Account):
    def calculate_interest(self):
        print("Fixed deposit interest calculated")

# 🚀 PART 4: Polymorphism in Action
accounts = [
    SavingsAccount(),
    FixedDeposit()
]
for acc in accounts:
    acc.calculate_interest()
# Output:
# Savings account interest calculated
# Fixed deposit interest calculated
# ✔ Same method call
# ✔ Different behavior
# ✔ Clean & scalable


# 1. Duck Typing (The Pythonic Way)
# In strictly typed languages (like Java), an object must belong to a specific class hierarchy to be treated polymorphically. In Python, as long as an object has the required method, Python will execute it.
class Bird:
    def fly(self):
        print("Flapping wings")
class Airplane:
    def fly(self):
        print("Engines roaring")
class Whale:
    def swim(self):
        print("Splashing water")
# This function doesn't care about the class type, only the behavior
def lift_off(entity):
    entity.fly()
bird = Bird()
plane = Airplane()
lift_off(bird)   # Works!
lift_off(plane)  # Works!
# lift_off(whale) would fail because whales don't have a fly() method.

# 2. Polymorphism with Inheritance
# This is the "standard" OOP approach. You define a method in a base class and override it in subclasses.
# Example: Payment Systems
# Imagine you are building a checkout system. You have different ways to pay, but the checkout process remains the same.
class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement this")
class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")
class PayPal(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")
# A single function can handle any payment type
def checkout(payment_method, amount):
    payment_method.process_payment(amount)
visa = CreditCard()
personal_paypal = PayPal()
checkout(visa, 100)            # Output: Processing credit card...
checkout(personal_paypal, 50)  # Output: Processing PayPal...

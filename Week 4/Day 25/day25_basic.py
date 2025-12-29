# 📅 DAY 25 — ENCAPSULATION (Data Protection & Control)

Encapsulation = Data + Protection
# It means:
# Do not allow direct access to sensitive data
# Force users to go through controlled methods
# Real life:
# ATM → you don’t touch bank database
# You use buttons (methods)

# ❌ PART 2: Problem Without Encapsulation
# class Account:
#     def __init__(self, balance):
#         self.balance = balance
# acc = Account(1000)
# acc.balance = -500   # ❌ dangerous
# This should never be allowed.

# 🔐 PART 3: Protected vs Private Attributes
# 1️⃣ Protected (_)
# self._balance
# Convention-based protection
# “Don’t touch unless you know what you’re doing”
# 2️⃣ Private (__)
# self.__balance
# Python applies name mangling
# Stronger protection

# 🔒 PART 4: Private Attribute Example
# class Account:
#     def __init__(self, balance):
#         self.__balance = balance
# This cannot be accessed directly:
# acc.__balance   # ❌ ERROR

# 🧠 PART 5: Getters & Setters (CONTROLLED ACCESS)
# class Account:
#     def __init__(self, balance):
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
# Now:
# balance can’t go negative
# rules are enforced

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")


acc = BankAccount("Raj", 1000)
acc.show_balance()

acc.deposit(500)
acc.withdraw(300)
acc.show_balance()


# Encapsulation prevents bugs by acting like a Security Guard (or a gatekeeper) for your data.
# In programming, the biggest source of bugs is "Uncontrolled Access." If any part of your code can reach into an object and change its variables directly, you will eventually break something.
# Here is exactly how encapsulation stops this, using a classic example: A Bank Account.
# The "Bad Way" (No Encapsulation)
# Imagine a class where anyone can touch the balance variable.
# class BankAccount:
#     def __init__(self):
#         self.balance = 1000  # Public variable (Unsafe)
# # --- The Bug Scenario ---
# my_acc = BankAccount()
# # ❌ BUG: A junior developer sets balance to a negative number directly!
# my_acc.balance = -5000 
# # Now the bank owes the customer money? Logic broken.
# # ❌ BUG: Someone accidentally sets it to a String
# my_acc.balance = "Five Thousand" 
# # The app crashes when we try to do math later.
# The Problem: There are no rules. The data is "naked."
# The "Good Way" (Encapsulation)
# Encapsulation fixes this by hiding the data (making it Private) and forcing everyone to use Methods (Functions) to change it.
# In Python, we use double underscores __ to make a variable private.
# class BankAccount:
#     def __init__(self):
#         self.__balance = 1000  # 🔒 PRIVATE variable (Hidden)
#     # ✅ The Gatekeeper for ADDING money
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}")
#         else:
#             print("❌ Error: Cannot deposit negative money!")
#     # ✅ The Gatekeeper for REMOVING money
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}")
#         else:
#             print("❌ Error: Insufficient funds or invalid amount.")
#     # ✅ The Safe Viewer (Read-Only)
#     def get_balance(self):
#         return self.__balance
# # --- Usage ---
# acc = BankAccount()
# # 🔒 Try to cheat?
# # acc.__balance = -5000  <-- ERROR! Python says this variable doesn't exist.
# # ✅ Use the methods
# acc.deposit(500)      # Works
# acc.withdraw(100000)  # Safe! The method catches the logic error.
# How does this prevent bugs?
# Validation Logic: The withdraw method checks if amount <= balance. You can't accidentally overdraw. If you had direct access, you might forget to check this condition in every part of your app.
# Read-Only Access: By using get_balance(), you allow people to see the money without letting them change it.
# Future-Proofing: If you later decide to charge a 1% fee on every withdrawal, you only change the code in one place (the withdraw method). Every part of your app updates automatically.
# The ML Connection (Your Field)
# Think about a Neural Network library like PyTorch.
# The Data: The Model Weights (The learned brain).
# The Protection: You are not supposed to manually type model.layer1.weight = 5. If you did, you would break the math.
# The Method: You call model.train(). This method safely updates the weights using complex calculus rules (Backpropagation), ensuring the model doesn't break.
# Summary: Encapsulation changes data from being a "Public Park" (anyone can walk in) to a "Vault" (you need the key/method to enter).

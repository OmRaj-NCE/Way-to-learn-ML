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

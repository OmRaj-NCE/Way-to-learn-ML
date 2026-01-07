class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate / 100
        self.balance += interest
        print("Interest added")


acc = SavingsAccount("Raj", 1000, 5)
acc.show_balance()
acc.add_interest()
acc.show_balance()

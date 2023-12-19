class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nNew Account '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, Account '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")
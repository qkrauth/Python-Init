from bank_accounts import *

Quinten = BankAccount(10000, "Quinten's Account")
John = BankAccount(5000, "Johns's Account")

Quinten.getBalance()
John.getBalance()

Quinten.deposit(5000)
John.deposit(2500)

Quinten.withdraw(5000)
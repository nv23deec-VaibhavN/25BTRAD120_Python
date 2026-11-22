class BankAccount:
def _init __ (self, account_holder, account_number, balance=0):
self.account_holder = account_holder
self.account_number = account_number
self ._ balance = balance # Private attribute (encapsulation)
def deposit(self, amount) :
if amount <= 0:
print("Invalid deposit amount.")
else:
self ._ balance += amount
print(f"Rs. {amount: .2f} deposited successfully.")
def withdraw(self, amount):
if amount <= 0:
print("Invalid withdrawal amount.")
elif amount > self ._ balance:
print("Insufficient balance.")
else:
self. balance -= amount
print(f"Rs. {amount: .2f} withdrawn successfully.")
def check_balance(self):
print(f"Available balance: Rs. {self ._ balance :. 2f}")
# Create an account object and perform sample transactions.
account = BankAccount("Aarav", "SB101", 5000)
print("ACCOUNT HOLDER:", account.account_holder)
print("ACCOUNT NUMBER:", account. account_number)
account.check_balance()
account .deposit (1500)
account.withdraw(2000)
account .withdraw(6000)  # Tests insufficient balance

account.deposit (-500)   # Tests invalid deposit

account .withdraw(0)

# Tests invalid withdrawal
account.check_balance()

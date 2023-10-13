

class BankAccount:
  def __init__(self):
       self.balance=0
       print("BankAccount Details")
  def deposit(self):
       amount=float(input("Enter the amount:"))
       self.balance+=amount
       print("amount is deposited in your account", amount)
  def withdraw (self):
       amount=float(input("Enter the amount:"))
       if self.balance>=amount:
        self.balance-=amount
        print("you withdraw:",amount)
       else:
        print("you don't have enough money")
  def display(self):
        print("Available Balance:",self.balance)
s=BankAccount()
s.deposit()
s.withdraw()
s.display()

      


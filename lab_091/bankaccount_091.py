class BankAccount(object):
   next_account_number = 16555232
   atype = "General"

   def __init__(self, first, sur, balance=0):
      self.first = first
      self.sur = sur
      self.account_number = BankAccount.next_account_number
      self.balance = balance
      BankAccount.next_account_number = BankAccount.next_account_number + 1

   def lodge(self, mon):
      self.balance = self.balance + mon

   def withdraw(self, mon):
      if 0 < self.balance - mon:
         self.balance = self.balance - mon
      else:
         print("Insufficient funds available")

   def __str__(self):
      l = []
      l.append("Name: {} {}".format(self.first, self.sur))
      l.append("Account number: {}".format(self.account_number))
      l.append("Account type: {}".format(BankAccount.atype))
      l.append("Balance: {:.2f}".format(self.balance))
      return "\n".join(l)

class CurrentAccount(BankAccount):
   overflow = 1000.00
   atype = "Current"

   def withdraw(self, mon):
      if -1000 < self.balance - mon:
         self.balance = self.balance - mon
      else:
         print("Insufficient funds available")

   def __str__(self):
      l = []
      l.append("Name: {} {}".format(self.first, self.sur))
      l.append("Account number: {}".format(self.account_number))
      l.append("Account type: {}".format(CurrentAccount.atype))
      l.append("Balance: {:.2f}".format(self.balance))
      l.append("Overdraft: {:.02f}".format(- CurrentAccount.overflow))
      return "\n".join(l)

class SavingsAccount(BankAccount):
   rate = 0.01
   atype = "Savings"

   def apply_interest(self):
      if 0 < self.balance * SavingsAccount.rate:
         self.balance = self.balance + (self.balance * SavingsAccount.rate)
      else:
         print("Insufficient funds available")

   def __str__(self):
      l = []
      l.append("Name: {} {}".format(self.first, self.sur))
      l.append("Account number: {}".format(self.account_number))
      l.append("Account type: {}".format(SavingsAccount.atype))
      l.append("Balance: {:.2f}".format(self.balance))
      l.append("Interest rate: {}".format(SavingsAccount.rate))
      return "\n".join(l)

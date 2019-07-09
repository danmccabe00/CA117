class BankAccount(object):
   next_account_number = 16555232
   total_lodgements = 0
   interest_rate = 0.043

   def __init__(self, first, sur, balance=0):
      self.first = first
      self.sur = sur
      self.account_number = BankAccount.next_account_number
      self.balance = balance
      BankAccount.next_account_number = BankAccount.next_account_number + 1

   def lodge(self, mon):
      self.balance = self.balance + mon
      BankAccount.total_lodgements = BankAccount.total_lodgements + 1

   def apply_interest(self):
      self.balance = self.balance + (self.balance * BankAccount.interest_rate)

   def __add__(self, m):
      self.balance = self.balance + m
      BankAccount.total_lodgements = BankAccount.total_lodgements + 1

   def __iadd__(self, other):
      self.balance = self.balance + other
      BankAccount.total_lodgements = BankAccount.total_lodgements + 1
      return self

   def __str__(self):
      l = []
      l.append("Name: {} {}".format(self.first, self.sur))
      l.append("Account number: {}".format(self.account_number))
      l.append("Balance: {:.2f}".format(self.balance))
      return "\n".join(l)

class BankAccount(object):

   def __init__(self, bal=0):
      self.bal = bal

   def withdraw(self, out):
      if out <= self.bal:
         self.bal = self.bal - out
      else:
         print("Insufficient funds available")

   def deposit(self, dep):
      self.bal = self.bal + dep

   def __str__(self):
         return "Your current balance is: {}.00 euro".format(str(self.bal))

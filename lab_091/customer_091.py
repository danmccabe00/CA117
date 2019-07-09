class Customer(object):

   discount = 0

   def __init__(self, name, money, ad1, ad2, ad3):
      self.name = name
      self.money = money
      self.ad1 = ad1
      self.ad2 = ad2
      self.ad3 = ad3
      self.due = 0

   def owes(self):
      self.due = self.money - (self.money * (self.discount / 100))
      return float(self.due)

   def __str__(self):
      l = []
      l.append("{}".format(self.name))
      l.append("{}".format(self.ad1))
      l.append("{}".format(self.ad2))
      l.append("{}".format(self.ad3))
      l.append("Balance: {:.02f}".format(float(self.money)))
      l.append("Discount: {}%".format(self.discount))
      l.append("Amount due: {:.02f}".format(self.owes()))
      return "\n".join(l)

class ValuedCustomer(Customer):

   discount = 10

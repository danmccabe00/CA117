class Element(object):

   def __init__(self, num, nam, sym, boil):
      self.num = num
      self.nam = nam
      self.sym = sym
      self.boil = boil

   def print_details(self):
      print("Number: {}".format(self.num))
      print("Name: {}".format(self.nam))
      print("Symbol: {}".format(self.sym))
      print("Boiling point: {} K".format(self.boil))

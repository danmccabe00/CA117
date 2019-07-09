class Employee(object):

   def __init__(self, name, number):
      self.name = name
      self.number = number

   def __str__(self):
      l = []
      l.append("Name: {}".format(self.name))
      l.append("Number: {}".format(self.number))
      l.append('Wages: {:.02f}'.format(0.00))
      return "\n".join(l)

class Manager(Employee):

   def __init__(self, name, number, floatsal):
      super().__init__(name, number)
      self.floatsal = floatsal

   def wage(self):
      wage = self.floatsal / 52
      return wage

   def __str__(self):
      l = []
      l.append("Name: {}".format(self.name))
      l.append("Number: {}".format(self.number))
      l.append('Wages: {:.02f}'.format(self.wage()))
      return "\n".join(l)

class AssemblyWorker(Employee):

   def __init__(self, name, number, rate, hours):
      super().__init__(name, number)
      self.rate = rate
      self.hours = hours

   def wage(self):
      wage = self.rate * self.hours
      return wage

   def __str__(self):
      l = []
      l.append("Name: {}".format(self.name))
      l.append("Number: {}".format(self.number))
      l.append('Wages: {:.02f}'.format(self.wage()))
      return "\n".join(l)

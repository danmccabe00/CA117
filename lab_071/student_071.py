class Student(object):

   def __init__(self, sur, fore, sid, mod=[]):
      self.sid = sid
      self.sur = sur
      self.fore = fore
      self.mod = mod

   def add_module(self, module):
      (self.mod).append(module)

   def del_module(self, module):
      if module in self.mod:
         (self.mod).remove(module)

   def print_details(self):
      print("ID: {}".format(self.sid))
      print("Surname: {}".format(self.sur))
      print("Forename: {}".format(self.fore))
      print("Modules: {}".format(" ".join(self.mod)))

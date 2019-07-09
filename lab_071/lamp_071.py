class Lamp(object):

   def __init__(self, stat=False):
      self.on = stat

   def turn_on(self):
      self.on = True

   def turn_off(self):
      self.on = False

   def toggle(self):
      if self.on is False:
         self.on = True
      elif self.on is True:
         self.on = False

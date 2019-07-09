class Point(object):

   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

   def reflect(self):
      self.x = -self.x
      self.y = -self.y

   def distance(self, other):
      return (((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)) ** (1 / 2)

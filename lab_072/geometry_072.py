class Point(object):

   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

   def distance(self, other):
      return (((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)) ** (1 / 2)

   def __str__(self):
      return "({}, {})".format(str(float(self.x)), str(float(self.y)))

class Segment(object):

   def __init__(self, x, y):
      self.p1 = x
      self.p2 = y

   def midpoint(self):
      x = (self.p1.x + self.p2.x) / 2
      y = (self.p1.y + self.p2.y) / 2
      return ("({}, {})".format(x, y))

      def length(self):
         return (((self.p2.x - self.p1.x) ** 2) + ((self.p2.y - self.p1.y) ** 2)) ** (1 / 2)

class Circle(object):

   def __init__(self, x, y):
      self.p1 = x
      self.r = y

   def overlaps(self, other):
      return (((other.p1.x - self.p1.x) ** 2) + ((other.p1.y - self.p1.y) ** 2)) ** (1 / 2) < other.r + self.r

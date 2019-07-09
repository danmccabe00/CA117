class Point(object):
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

   def midpoint(self, other):
      x = (self.x + other.x) / 2
      y = (self.y + other.y) / 2
      return Point(x, y)

   def __str__(self):
      return ("({}, {})".format(self.x, self.y))


class Circle(object):
   def __init__(self, p, radius=0):
      self.p = p
      self.radius = radius

   def __add__(self, other):
      p = Point.midpoint(self.p, other.p)
      radius = self.radius + other.radius
      return ("Centre: ({}, {})".format(p.x, p.y)) + "\n" + "Radius: {}".format(radius)

   def __str__(self):
      return ("Centre: ({:1f}, {:1f})".format(self.p.x, self.p.y)) + "\n" + "Radius: {}".format(self.radius)

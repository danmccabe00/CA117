class Shape(object):

   def __init__(self, point):
      self.point = point

   def sides(self):
      l = []
      i = -1
      while i < len(self.point) - 1:
         l.append(Point.distance(self.point[i], self.point[i + 1]))
         i = i + 1
      j = 0
      while j < len(l) + 1:
         l.append(l[0])
         l.pop(0)
         j = j + 1
      self.l = l
      return l

   def perimeter(self):
      tot = 0
      for nums in self.l:
         tot = tot + nums
      return tot

class Point(Shape):

   def __init__(self, floatx, floaty):
      self.floatx = floatx
      self.floaty = floaty

   def distance(self, other):
     return float((((self.floatx - other.floatx) ** 2) + ((self.floaty - other.floaty) ** 2)) ** (1 / 2))

class Triangle(Shape):

   def area(self):
      s = (self.l[0] + self.l[1] + self.l[2]) / 2
      self.area = (s * (s - self.l[0]) * (s - self.l[1]) * (s - self.l[2])) ** 0.5
      return self.area

class Square(Shape):

   def area(self):
      self.area = self.l[0] ** 2
      return self.area

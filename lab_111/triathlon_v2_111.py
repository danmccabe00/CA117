class Triathlete(object):

   def __init__(self, name, tid):
      self.name = name
      self.tid = tid

   def __str__(self):
      l = []
      l.append("Name: {}".format(self))
      l.append("ID: {}".format(self))
      return "\n".join(l)

class Triathlon(Triathlete):

   def __init__(self):
      self.d = {}

   def add(self, t1):
      self.d[t1.tid] = t1

   def lookup(self, t1):
      try:
         return self.d[t1]
      except:
         return None

   def __str__(self):
      l = []
      for ath in sorted(self.d.values(), key=lambda x: x.name):
         l.append("Name: {}".format(ath.name))
         l.append("ID: {}".format(ath.tid))
      return "\n".join(l)

   def remove(self, t1):
      del self.d[t1]

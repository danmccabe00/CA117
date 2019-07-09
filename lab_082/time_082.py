class Time(object):

   def __init__(self, hours=0, minutes=0, seconds=0):
      self.seconds = seconds
      self.minutes = minutes
      self.hours = hours

   def __str__(self):
      return "The time is {:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)

   def __eq__(self, other):
      tself = self.seconds + (self.minutes * 60) + (self.hours * 60 * 60)
      tother = other.seconds + (other.minutes * 60) + (other.hours * 60 * 60)
      return tself == tother

   def __gt__(self, other):
      tself = self.seconds + (self.minutes * 60) + (self.hours * 60 * 60)
      tother = other.seconds + (other.minutes * 60) + (other.hours * 60 * 60)
      return tself > tother

   def __add__(self, other):
      tself = self.seconds + (self.minutes * 60) + (self.hours * 60 * 60)
      tother = other.seconds + (other.minutes * 60) + (other.hours * 60 * 60)
      tot = tself + tother
      minute, second = divmod(tot, 60)
      hour, minute = divmod(minute, 60)
      overflow, hour = divmod(hour, 24)
      return Time(hour, minute, second)

   def __iadd__(self, other):
      z = self + other
      self.hours, self.minutes, self.seconds = z.hours, z.minutes, z.seconds
      return self

   def seconds_to_time(tot):
      minute, second = divmod(tot, 60)
      hour, minute = divmod(minute, 60)
      overflow, hour = divmod(hour, 24)
      return Time(hour, minute, second)

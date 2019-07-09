class Score(object):

   def __init__(self, goals=0, pints=0):
      self.goals = goals
      self.pints = pints

   def greater_than(self, other):
      return (other.goals * 3) + other.pints < (self.goals * 3) + self.pints

   def less_than(self, other):
      return (other.goals * 3) + other.pints > (self.goals * 3) + self.pints

   def equal_to(self, other):
      return (other.goals * 3) + other.pints == (self.goals * 3) + self.pints

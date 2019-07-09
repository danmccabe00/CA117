class Score(object):
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return "{} goal(s) and {} point(s)".format(self.goals, self.points)

    def __eq__(self, other):
        return ((self.goals * 3) + self.points) == ((other.goals * 3) + other.points)

    def __gt__(self, other):
        return ((self.goals * 3) + self.points) > ((other.goals * 3) + other.points)

    def __ge__(self, other):
        return ((self.goals * 3) + self.points) >= ((other.goals * 3) + other.points)

    def __add__(self, other):
        goals = self.goals + other.goals
        points = self.points + other.points
        return Score(goals, points)

    def __sub__(self, other):
        goals = self.goals - other.goals
        points = self.points - other.points
        return Score(goals, points)

    def __iadd__(self, other):
        z = self + other
        self.goals, self.points = z.goals, z.points
        return self

    def __isub__(self, other):
        z = self - other
        self.goals, self.points = z.goals, z.points
        return self

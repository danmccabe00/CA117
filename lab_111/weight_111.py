class Weight(object):

    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces
        self.weight = (pounds * 16) + ounces

    def from_ounces(ounces=0):
        pounds = ounces // 16
        ounces = ounces % 16
        return Weight(pounds, ounces)

    def __str__(self):
        return "{} pound(s) and {} ounce(s)".format(self.pounds, self.ounces)

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __iadd__(self, other):
        z = self + other
        self.pounds = z.pounds
        self.ounces = z.ounces
        self.weight = z.weight
        return self

    def __mul__(self, num):
        return Weight.from_ounces(self.weight * num)

    def __add__(self, other):
        w = (self.pounds * 16) + (other.pounds * 16) + self.ounces + other.pounds
        pounds = w // 16
        ounces = (w % 16) - 2
        return Weight(pounds, ounces)

from FUNCTIONS import find_h_cost
class node(object):
    def __init__(self, x, y, traversable=True):
        self.x = x
        self.y = y
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0
        self.prev_node = None
        self.traversable = traversable
        self.evaluated = False

    def evaluate(self):
        self.evaluated = True

    def set_h_cost(self, end):
        self.h_cost = find_h_cost(self, end)

    def set_g_cost(self):
        return

    def set_f_cost(self):
        self.f_cost = self.h_cost + self.g_cost
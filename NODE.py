class node(object):
    def __init__(self, x, y, g_cost=0):
        self.x = x
        self.y = y
        self.g_cost = g_cost
        self.h_cost = 0
        self.f_cost = 0
        self.prev_node = None
        self.evaluated = False

    def evaluate(self):
        self.evaluated = True

    def set_g_cost(self):
        return

    def set_f_cost(self):
        self.f_cost = self.h_cost + self.g_cost

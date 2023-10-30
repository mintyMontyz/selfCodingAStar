from NODE import node
def find_h_cost(node, end):
    dist = 0
    while node.x != end.x or node.y != end.y:

        if node.x == end.x:
            dist += abs(end.y - node.y)*10
            return dist

        elif node.y == end.y:
            dist += abs(end.x - node.x)*10
            return dist

        else:
            if end.x > node.x and end.y > node.y:
                node.x += 1
                node.y += 1

            elif end.x > node.x and end.y < node.y:
                node.x += 1
                node.y -= 1

            elif end.x < node.x and end.y < node.y:
                node.x -= 1
                node.y -= 1

            elif end.x < node.x and end.y > node.y:
                node.x -= 1
                node.y += 1

            dist += 14


    return dist

def node_min_f_cost(matrix):
    fcost = matrix[0].f_cost
    obj = matrix[0]
    for i in matrix:
        if i.f_cost < fcost:
            obj = i
            fcost = i.f_cost

    return obj

def add_neighbour(current, open, closed, non_traversable):
    to_be_added = [node(current.x - 1, current.y, current.g_cost+10), node(current.x - 1, current.y - 1, current.g_cost+14),
                   node(current.x - 1, current.y + 1, current.g_cost+14), node(current.x, current.y + 1, current.g_cost+10), node(current.x, current.y - 1, current.g_cost+10),
                   node(current.x + 1, current.y, current.g_cost+10), node(current.x + 1, current.y - 1, current.g_cost+14),
                   node(current.x + 1, current.y + 1, current.g_cost+14)]


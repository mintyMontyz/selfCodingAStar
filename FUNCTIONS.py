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

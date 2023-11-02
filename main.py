from FUNCTIONS import *

WIDTH, HEIGHT = 20, 20


def main():
    matrix_field = [[node(i, j) for i in range(WIDTH)] for j in range(HEIGHT)]

    open_matrix = []  # open needs to be evaluated

    closed_matrix = []  # closed already evaluated

    start = return_node_from_pos(7, 2, matrix_field)
    end = return_node_from_pos(5, 1, matrix_field)

    open_matrix.append(start)

    while True:

        current = node_min_f_cost(open_matrix)
        open_matrix.remove(current)
        closed_matrix.append(current)

        if current == end:
            print(retrace_path(start, end))
            print(closed_matrix)
            return

        for neighbour in get_neighbour(current, matrix_field):
            if not neighbour.traversable or neighbour in closed_matrix:
                continue

            new_move_cost_to_neighbour = current.g_cost + find_dist(current, neighbour)
            if new_move_cost_to_neighbour < neighbour.g_cost or neighbour not in open_matrix:
                neighbour.g_cost = new_move_cost_to_neighbour
                neighbour.h_cost = find_dist(neighbour, end)
                neighbour.parent_node = current

                if neighbour not in open_matrix:
                    open_matrix.append(neighbour)


if __name__ == "__main__":
    main()

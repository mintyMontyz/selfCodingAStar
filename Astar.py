from FUNCTIONS import *


def run_a_star(start_vector, end_vector, dimensions, obstacle_list):
    matrix_field = [[node(x, y) for x in range(dimensions[0])] for y in range(dimensions[1])]

    if obstacle_list is not None:
        for i in obstacle_list:
            matrix_field[i[0]][i[1]].traversable = False

    open_matrix = []  # open needs to be evaluated

    closed_matrix = []  # closed already evaluated

    start = return_node_from_pos(start_vector[0], start_vector[1], matrix_field)
    end = return_node_from_pos(end_vector[0], end_vector[1], matrix_field)

    open_matrix.append(start)

    while True:

        current = node_min_f_cost(open_matrix)
        open_matrix.remove(current)
        closed_matrix.append(current)

        if current == end:
            return retrace_path(start, end), matrix_field, open_matrix, closed_matrix, start, end

        for neighbour in get_neighbour(current, matrix_field):
            if not neighbour.traversable or neighbour in closed_matrix:
                continue

            new_move_cost_to_neighbour = current.g_cost + find_dist(current, neighbour)
            if new_move_cost_to_neighbour < neighbour.g_cost or (neighbour not in open_matrix):
                neighbour.g_cost = new_move_cost_to_neighbour
                neighbour.h_cost = find_dist(neighbour, end)
                neighbour.parent_node = current

                if neighbour not in open_matrix:
                    open_matrix.append(neighbour)

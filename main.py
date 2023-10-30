from FUNCTIONS import *

START = node(0, 0)
END = node(0, 1)

open_matrix = []  # open needs to be evaluated

closed_matrix = []  # closed already evaluated

non_traversable = []

open_matrix.append(START)

def main():
    current = node_min_f_cost(open_matrix)
    open_matrix.remove(current)
    closed_matrix.append(current)

    if current.x == END.x and current.y == END.y:
        print("finished")
        return


if __name__ == "__main__":
    main()

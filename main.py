from NODE import node

import numpy as np

START = node(0, 0)
END = node(5, -2)

open_matrix = []  # open needs to be evaluated

closed_matrix = []  # closed already evaluated

open_matrix.append(START)

def main():
    START.set_h_cost(END)
    print(START.h_cost)

if __name__ == "__main__":
    main()

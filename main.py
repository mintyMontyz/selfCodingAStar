import pygame as pg
import pygame.draw

from Astar import run_a_star

pg.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

WHITE, BLACK, RED, GREEN, PURPLE, BLUE, YELLOW = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (255, 0, 247), (0, 43, 255), (255, 205, 0)

node_count_x, node_count_y = 20, 20

start_vec = (0, 3)
end_vec = (8, 19)


class drawn_node(object):
    def __init__(self, x_, y_, size_x, size_y):
        self.x = x_
        self.y = y_
        self.size_x = size_x
        self.size_y = size_y
        self.colour = None

    def update(self, colour_code):
        if colour_code == 0:
            self.colour = WHITE  # nothing
        elif colour_code == 1:
            self.colour = GREEN  # open
        elif colour_code == 2:
            self.colour = RED  # closed
        elif colour_code == 3:
            self.colour = BLACK  # non traversable
        elif colour_code == 4:
            self.colour = PURPLE  # start
        elif colour_code == 5:
            self.colour = BLUE  # end
        elif colour_code == 6:
            self.colour = YELLOW  # path

    def draw(self, screen_):
        pg.draw.rect(screen_, self.colour, (self.x, self.y, self.size_x, self.size_y))


def create_drawn_nodes(space_between_nodes):
    size_x = SCREEN_WIDTH//node_count_x - space_between_nodes
    size_y = SCREEN_HEIGHT//node_count_y - space_between_nodes

    drawn_nodes = [[drawn_node(x * (size_x + space_between_nodes) + space_between_nodes//2, y * (size_y + space_between_nodes) + space_between_nodes//2, size_x, size_y) for x in range(node_count_x)] for y in range(node_count_y)]

    return drawn_nodes


draw_nodes = create_drawn_nodes(10)


def colour_nodes(path, matrix, open_, closed, start_, end_):
    for x in range(len(draw_nodes)):
        for y in range(len(draw_nodes[x])):
            draw_nodes[x][y].update(0)
            if matrix[x][y] in open_:
                draw_nodes[x][y].update(1)
            if matrix[x][y] in closed:
                draw_nodes[x][y].update(2)
            if matrix[x][y] in path:
                draw_nodes[x][y].update(6)
            if not matrix[x][y].traversable:
                draw_nodes[x][y].update(3)
            if matrix[x][y] == start_:
                draw_nodes[x][y].update(4)
            if matrix[x][y] == end_:
                draw_nodes[x][y].update(5)


def show():
    screen.fill(BLACK)
    for x in range(len(draw_nodes)):
        for y in range(len(draw_nodes[x])):
            draw_nodes[x][y].draw(screen)

    pg.display.flip()


def main():
    path_, matrix_, open_, closed_, start_, end_ = run_a_star(start_vec, end_vec, (20, 20))
    colour_nodes(path_, matrix_, open_, closed_, start_, end_)

    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print("x = {}, y = {}".format(pos[0], pos[1]))
        show()

    pg.quit()


if __name__ == "__main__":
    main()
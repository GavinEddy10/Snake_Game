from Snake import *


class Game:

    def __init__(self):
        self.rows = 15
        self.cols = 17
        self.board = self.create_2D_array()
        self.snake = Snake(Cell(3, 3))

    def act(self, screen):
        self.snake.draw(screen)

    def create_2D_array(self):
        # Declaring an empty 1D array.
        a = []
        # Declaring an empty 1D array.
        b = []
        # Initialize the column.
        for j in range(0, self.cols):
            b.append(0)
        # Append the column to each row.
        for i in range(0, self.rows):
            a.append(b)
        return a

# works
    def print_array(self):
        print(self.board)

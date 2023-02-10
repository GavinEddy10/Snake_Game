import pygame.draw as balls


class Snake:

    def __init__(self, head):
        self.size = 0
        self.direction = 'D'
        self.head = head
        self.body = [head, Cell(2, 3), Cell(1, 3)] # list of cells

    def move(self): # use direction
        pass

    def draw(self,screen):
        balls.rect(screen, ())

    def get_list(self):
        return self.body

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        if direction == 'W' or direction == 'D' or direction == 'A' or direction == 'A':
            self.direction = direction

    def get_head(self):
        return self.head


class Cell:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def set_row(self, row):
        self.row = row

    def set_col(self, col):
        self.col = col
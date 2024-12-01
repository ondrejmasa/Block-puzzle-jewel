import pygame
from parameters import *


class SmallGrid:
    def __init__(self):
        self.num_rows = 4
        self.num_cols = 12
        self.cell_size = 33
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(small_startpoint_x + col * self.cell_size, small_startpoint_y + row * self.cell_size, self.cell_size - 1,
                                        self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

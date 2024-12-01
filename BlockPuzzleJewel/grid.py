import pygame
from parameters import Colors


class Grid:
    def __init__(self):
        self.num_rows = 8
        self.num_cols = 8
        self.cell_size = 50
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def is_inside(self, row, col):
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            return True
        return False

    def is_empty(self, row, col):
        if self.grid[row][col] == 0:
            return True
        return False

    def is_full_row(self, row):
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:
                return False
        return True

    def is_full_col(self, col):
        for row in range(self.num_rows):
            if self.grid[row][col] == 0:
                return False
        return True

    def clear_row(self, row):
        for col in range(self.num_cols):
            self.grid[row][col] = 0

    def clear_col(self, col):
        for row in range(self.num_rows):
            self.grid[row][col] = 0

    def clear_full_rows_and_cols(self):
        completed = 0
        rows = []
        cols = []
        for row in range(self.num_rows):
            if self.is_full_row(row):
                rows.append(row)
                completed += 1
        for col in range(self.num_cols):
            if self.is_full_col(col):
                cols.append(col)
                completed += 1
        for row in rows:
            self.clear_row(row)
        for col in cols:
            self.clear_col(col)
        return completed

    def restart(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(11 + col * self.cell_size, 11 + row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
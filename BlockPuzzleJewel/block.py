from parameters import Colors
from position import Position
import pygame


class Block:
    def __init__(self, id, cell_size):
        self.id = id
        self.cells = []
        self.cell_size = cell_size
        self.row_offset = 0
        self.col_offset = 0
        self.can_be_placed = True
        self.colors = Colors.get_cell_colors()

    def move(self, rows, cols):
        self.row_offset += rows
        self.col_offset += cols

    def get_cell_positions(self):
        tiles = self.cells
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.col + self.col_offset)
            moved_tiles.append(position)
        return moved_tiles

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            surface = pygame.Surface((self.cell_size-1, self.cell_size-1), pygame.SRCALPHA)
            surface.fill(self.colors[self.id] + (128,))
            screen.blit(surface, (offset_x + tile.col * self.cell_size, offset_y + tile.row * self.cell_size))
            # tile_rect = pygame.Rect(offset_x + tile.col * self.cell_size, offset_y + tile.row * self.cell_size, self.cell_size-1, self.cell_size-1)
            # pygame.draw.rect(screen, self.colors[self.id] + (50,), tile_rect)
            pygame.draw.circle(screen, Colors.white, (offset_x + tile.col * self.cell_size + self.cell_size // 2,
                                                      offset_y + tile.row * self.cell_size + self.cell_size // 2), 3)

    def draw_small(self, screen, offset_x, offset_y, chosen):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.col * self.cell_size, offset_y + tile.row * self.cell_size,
                                    self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, Colors.green if self.can_be_placed else Colors.red, tile_rect)
            if chosen:
                pygame.draw.circle(screen, Colors.white, (offset_x + tile.col * self.cell_size + self.cell_size//2,
                                   offset_y + tile.row * self.cell_size + self.cell_size//2), 3)

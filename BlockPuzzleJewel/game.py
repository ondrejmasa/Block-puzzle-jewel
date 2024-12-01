import pygame
from grid import Grid
from small_grid import SmallGrid
from blocks import *
from parameters import *
import random


class Game:
    def __init__(self):
        self.grid = Grid()
        self.small_grid = SmallGrid()
        self.blocks = [IBlock(cell_size), JBlock(cell_size), LBlock(cell_size), OBlock(cell_size), SBlock(cell_size),
                       TBlock(cell_size), ZBlock(cell_size), FullBlock(cell_size), CornerBlock(cell_size),
                       BigCornerBlock(cell_size), OneBlock(cell_size), TwoBlock(cell_size), ThreeBlock(cell_size)]
        self.small_blocks = [IBlock(small_cell_size), JBlock(small_cell_size), LBlock(small_cell_size),
                             OBlock(small_cell_size), SBlock(small_cell_size), TBlock(small_cell_size), ZBlock(small_cell_size),
                             FullBlock(small_cell_size), CornerBlock(small_cell_size), BigCornerBlock(small_cell_size),
                             OneBlock(small_cell_size), TwoBlock(small_cell_size), ThreeBlock(small_cell_size)]
        self.blocks_to_place = self.get_random_small_blocks()
        self.chosen_block_index = 0
        self.current_block = None
        self.choosing = True
        self.game_over = False
        self.score = 0
        self.clear_sound = pygame.mixer.Sound("sounds/Sounds_clear.ogg")

        pygame.mixer.music.load("sounds/background.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)

    def count_score(self, cleared):
        if cleared == 1:
            self.score += 100
        elif cleared == 2:
            self.score += 300
        elif cleared == 3:
            self.score += 500
        elif cleared > 3:
            self.score += 1000

    def get_random_small_blocks(self):
        block1 = random.choice(self.small_blocks)
        block2 = random.choice(self.small_blocks)
        block3 = random.choice(self.small_blocks)
        if block1 != block2 or block2 != block3:
            return [block1, block2, block3]
        else:
            return self.get_random_small_blocks()

    def change_chosen_block(self):
        self.chosen_block_index += 1
        if self.chosen_block_index > 2:
            self.chosen_block_index = 0
        chosen_block = self.blocks_to_place[self.chosen_block_index]
        while chosen_block is None or not chosen_block.can_be_placed:
            self.chosen_block_index += 1
            if self.chosen_block_index > 2:
                self.chosen_block_index = 0
            chosen_block = self.blocks_to_place[self.chosen_block_index]

    def get_current_block(self):
        chosen = self.blocks_to_place[self.chosen_block_index]
        index = self.small_blocks.index(chosen)
        self.current_block = self.blocks[index]
        self.choosing = False
        self.blocks_to_place[self.chosen_block_index] = None

    def block_inside(self, block):
        tiles = block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.col):
                return False
        return True

    def block_fits(self, block):
        tiles = block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.col):
                return False
        return True

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside(self.current_block):
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside(self.current_block):
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside(self.current_block):
            self.current_block.move(-1, 0)

    def move_up(self):
        self.current_block.move(-1, 0)
        if not self.block_inside(self.current_block):
            self.current_block.move(1, 0)

    def lock_block(self):
        if self.block_fits(self.current_block):
            tiles = self.current_block.get_cell_positions()
            for position in tiles:
                self.grid.grid[position.row][position.col] = self.current_block.id
            self.current_block.row_offset = self.current_block.col_offset = 0
            self.current_block = None
            self.choosing = True
            num_of_cleared = self.grid.clear_full_rows_and_cols()
            if num_of_cleared > 0:
                self.clear_sound.play()
            self.count_score(num_of_cleared)
            if self.blocks_to_place.count(None) == len(self.blocks_to_place):
                self.blocks_to_place = self.get_random_small_blocks()
                self.chosen_block_index = 2
            can_be_placed = []
            for block in self.blocks_to_place:
                if block is not None:
                    can = self.can_block_be_placed(block)
                    if not can:
                        block.can_be_placed = False
                    else:
                        block.can_be_placed = True
                    can_be_placed.append(can)
            if can_be_placed.count(False) == len(can_be_placed):
                self.game_over = True
            else:
                self.change_chosen_block()

    def can_block_be_placed(self, block):
        for row in range(self.grid.num_rows):
            block.row_offset = row
            for col in range(self.grid.num_cols):
                block.col_offset = col
                if self.block_inside(block) and self.block_fits(block):
                    block.row_offset = 0
                    block.col_offset = 0
                    return True
        block.row_offset = 0
        block.col_offset = 0
        return False

    def restart(self):
        self.grid.restart()
        self.blocks_to_place = self.get_random_small_blocks()
        self.chosen_block_index = 0
        self.current_block = None
        self.choosing = True
        self.game_over = False
        self.score = 0
        for block in self.blocks_to_place:
            block.can_be_placed = True

    def draw(self, screen):
        self.grid.draw(screen)
        self.small_grid.draw(screen)
        i = 0
        for block in self.blocks_to_place:
            if block is None:
                i += 1
                continue
            is_chosen = i == self.chosen_block_index
            if block.id in [1, 7, 11, 6, 5, 2, 3]:     # move down
                block.draw_small(screen, small_startpoint_x + i * 4 * block.cell_size, block.cell_size + small_startpoint_y, is_chosen)
            elif block.id in [13, 12, 4, 9]:        # move down and right
                block.draw_small(screen, 33 + small_startpoint_x + i * 4 * block.cell_size, block.cell_size + small_startpoint_y, is_chosen)

            else:
                block.draw_small(screen, small_startpoint_x + i * 132, small_startpoint_y, is_chosen)
            i += 1

        if self.current_block:
            self.current_block.draw(screen, startpoint_x, startpoint_y)

import random
import os
from utils import BOARD_SIZE, random_tile

class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.score = 0
        self.best_score = self.load_best_score()

        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        empty = []

        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self.grid[r][c] == 0:
                    empty.append((r, c))

        if empty:
            r, c = random.choice(empty)
            self.grid[r][c] = random_tile()

    def compress(self, row):
        new = [x for x in row if x != 0]

        i = 0
        while i < len(new) - 1:
            if new[i] == new[i + 1]:
                new[i] *= 2
                self.score += new[i]
                if self.score > self.best_score:
                     self.best_score = self.score
                     self.save_best_score()
                new.pop(i + 1)
            i += 1

        while len(new) < BOARD_SIZE:
            new.append(0)

        return new

    def move_left(self):
        moved = False

        new_grid = []

        for row in self.grid:
            compressed = self.compress(row)

            if compressed != row:
                moved = True

            new_grid.append(compressed)

        self.grid = new_grid

        if moved:
            self.spawn_tile()

        return moved
    
    def reverse(self):
         self.grid = [row[::-1] for row in self.grid]

    def transpose(self):
        self.grid = [list(row) for row in zip(*self.grid)]

    def move_right(self):
        self.reverse()
        moved = self.move_left()
        self.reverse()
        return moved

    def move_up(self):
        self.transpose()
        moved = self.move_left()
        self.transpose()
        return moved

    def move_down(self):
        self.transpose()
        self.reverse()
        moved = self.move_left()
        self.reverse()
        self.transpose()
        return moved

    def has_won(self):
        for row in self.grid:
            if 2048 in row:
                return True
        return False

    def has_moves(self):
        for row in self.grid:
            if 0 in row:
                return True

        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE - 1):
                if self.grid[r][c] == self.grid[r][c + 1]:
                    return True

        for c in range(BOARD_SIZE):
            for r in range(BOARD_SIZE - 1):
                if self.grid[r][c] == self.grid[r + 1][c]:
                    return True

        return False

    def reset(self):
        self.grid = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.score = 0
        self.best_score = self.load_best_score()
        self.spawn_tile()
        self.spawn_tile()
    
    def save_best_score(self):
         with open("best_score.txt", "w") as file:
              file.write(str(self.best_score))

    def load_best_score(self):
         if os.path.exists("best_score.txt"):
                with open("best_score.txt", "r") as file:
                  return int(file.read())
         return 0
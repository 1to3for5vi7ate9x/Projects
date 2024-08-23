import random
import numpy as np

class Game2048:
    def __init__(self):
        self.grid = np.zeros((4, 4), dtype=int)
        self.grid[0, 3] = 4  # Start with 4 at the right corner
        self.score = 0

    def add_new_tile(self):
        empty_cells = list(zip(*np.where(self.grid == 0)))
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.grid[x, y] = 2 if random.random() < 0.9 else 4

    def move(self, direction):
        original_grid = self.grid.copy()
        if direction in ['left', 'right']:
            self.grid = np.flip(self.grid, axis=1) if direction == 'right' else self.grid
            for i in range(4):
                self.grid[i] = self.merge(self.grid[i])
            self.grid = np.flip(self.grid, axis=1) if direction == 'right' else self.grid
        else:  # up or down
            self.grid = np.flip(self.grid.T, axis=1) if direction == 'down' else self.grid.T
            for i in range(4):
                self.grid[i] = self.merge(self.grid[i])
            self.grid = np.flip(self.grid, axis=1).T if direction == 'down' else self.grid.T
        
        if not np.array_equal(original_grid, self.grid):
            self.add_new_tile()
        return not np.array_equal(original_grid, self.grid)

    def merge(self, row):
        row = row[row != 0]
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                row[i] *= 2
                self.score += row[i]
                row[i + 1] = 0
        row = row[row != 0]
        return np.pad(row, (0, 4 - len(row)), 'constant')

    def is_game_over(self):
        if 0 in self.grid:
            return False
        for i in range(4):
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j + 1] or self.grid[j][i] == self.grid[j + 1][i]:
                    return False
        return True

    def get_max_tile(self):
        return np.max(self.grid)

def ai_play(game):
    directions = ['left', 'right', 'up', 'down']
    while not game.is_game_over():
        best_direction = max(directions, key=lambda d: evaluate_move(game, d))
        if not game.move(best_direction):
            break
    return game.score, game.get_max_tile()

def evaluate_move(game, direction):
    test_game = Game2048()
    test_game.grid = game.grid.copy()
    test_game.score = game.score
    if test_game.move(direction):
        return test_game.score + np.sum(test_game.grid) + corner_bonus(test_game.grid)
    return -1

def corner_bonus(grid):
    return grid[0, 0] * 2 + grid[0, 3] * 1.5 + grid[3, 0] * 1.5 + grid[3, 3]

# Play the game
game = Game2048()
final_score, max_tile = ai_play(game)
print(f"Game Over! Score: {final_score}, Max Tile: {max_tile}")
print(game.grid)

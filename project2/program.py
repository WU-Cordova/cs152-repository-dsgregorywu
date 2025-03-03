#export PYTHONPATH=$PYTHONPATH:/derecgregory/Documents/GitHub/cs152-repository-dsgregorywu/datastructures

import random
import time
import copy
from datastructures.array2d import Array2D
from kbhit import KBHit

columns = 25
rows = 30

class Cell:
    """Defines a cell within a grid."""
    def __init__(self, x, y, alive=False):
        self.xpos = x
        self.ypos = y
        self.alive = alive

    def detect_neighbors(self, grid):
        """Detects how many neighbors a cell has."""
        neighbors = 0
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for dx, dy in directions:
            nx, ny = self.xpos + dx, self.ypos + dy
            if 0 <= nx < grid.cellgrid.column_len and 0 <= ny < grid.cellgrid.row_len and grid.cellgrid[nx][ny].alive:
                neighbors += 1
        return neighbors

class Grid:
    """Defines a grid of cells in a generation."""
    def __init__(self, rows, columns, generation=0):
        self.rows = rows
        self.columns = columns
        self.generation = generation
        self.cellgrid = Array2D([[Cell(x, y, False) for y in range(rows)] for x in range(columns)])

    def update_grid(self):
        """Creates a new Grid object for the next generation."""
        new_cellgrid = Array2D([[Cell(x, y, False) for y in range(self.rows)] for x in range(self.columns)])
        for x in range(self.columns):
            for y in range(self.rows):
                cell = self.cellgrid[x][y]
                neighbors = cell.detect_neighbors(self)
                next_alive = (neighbors == 3) or (cell.alive and neighbors in [2, 3])
                new_cellgrid[x][y].alive = next_alive
        return Grid(self.rows, self.columns, self.generation + 1)

    def is_identical(self, other):
        """Compares two grids to check if they are identical."""
        for x in range(self.columns):
            for y in range(self.rows):
                if self.cellgrid[x][y].alive != other.cellgrid[x][y].alive:
                    return False
        return True

class GameController:
    """Controls the game."""
    def __init__(self):
        self.history = []
        self.endmessage = ""
        self.kb = KBHit()
        self.choose_mode()
        self.grid = self.start_colony()
        self.run_game()
        
    def choose_mode(self):
        while True:
            response = input("Welcome to the Game of Life! (A)utomatic, (M)anual, or (Q)uit? ").strip().upper()
            if response in ["A", "M", "Q"]:
                self.mode = "Automatic" if response == "A" else "Manual" if response == "M" else exit()
                break
            print("Invalid input. Type 'A', 'M', or 'Q'.")

    def start_colony(self):
        grid = Grid(rows, columns)
        response = input("Would you like a (R)andom start or (F)ile input? ").strip().upper()
        print(" ")
        if response == "R":
            for x in range(grid.columns):
                for y in range(grid.rows):
                    grid.cellgrid[x][y].alive = random.choice([True, False])
        elif response == "F":
            filename = input("Enter the filename: ").strip()
            try:
                with open(filename, 'r') as file:
                    for y, line in enumerate(file):
                        for x, char in enumerate(line.strip()):
                            if x < columns and y < rows:
                                grid.cellgrid[x][y].alive = (char == 'O')
            except FileNotFoundError:
                print("File not found. Starting with a random colony.")
                return self.start_colony()
        else:
            print("Invalid choice. Please select (R)andom or (F)ile.")
            return self.start_colony()
        return grid

    def run_game(self):
        while True:
            self.history.append(copy.deepcopy(self.grid))
            if len(self.history) > 5:
                self.history.pop(0)
            self.display_grid()
            if self.check_stability():
                print(self.endmessage)
                break
            self.grid = self.grid.update_grid()
            if self.mode == "Manual":
                self.wait_for_manual_input()
            else:
                time.sleep(1)

    def display_grid(self):
        """Prints the current generation."""
        print(f"Generation {self.grid.generation}")
        for y in range(self.grid.cellgrid.row_len):
            for x in range(self.grid.cellgrid.column_len):
                cell = self.grid.cellgrid[x, y]  
                print("🦠" if cell.alive else " ", end=" ")
            print()

    def check_stability(self):
        """Checks if the grid has become stable or is repeating."""
        empty = True
        for x in range(self.columns):
            for y in range(self.rows):
                if self.history[-1].alive == True:
                    empty = False
        if empty == True: 
            self.endmessage = "No life detected. Simulation ended."
            return True
        if len(self.history) < 3:
            return False
        if self.history[-1].is_identical(self.history[-2]):
            self.endmessage = "Stable pattern detected. Simulation ended."
            return True 
        if len(self.history) >= 3 and self.history[-1].is_identical(self.history[-3]):
            self.endmessage = "Repeating pattern detected. Simulation ended."
            return True 
        return False

    def wait_for_manual_input(self):
        """Handles manual stepping through generations."""
        print("Press 'N' for next, 'A' for automatic, 'Q' to quit.")
        while not self.kb.kbhit():
            time.sleep(0.1)
        key = self.kb.getch().lower()
        if key == 'q':
            exit()
        elif key == 'a':
            self.mode = "Automatic"
            print("Switched to Automatic mode.")
        elif key != 'n':
            print("Invalid key. Use 'N' to step, 'A' for auto, 'Q' to quit.")

if __name__ == "__main__":
    GameController()

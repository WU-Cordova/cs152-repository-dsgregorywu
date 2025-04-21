#export PYTHONPATH=$PYTHONPATH:/derecgregory/Documents/GitHub/cs152-repository-dsgregorywu/datastructures
import random
import time
import copy
from datastructures.array2d import Array2D
from projects.project2.kbhit import KBHit

importedfile = "testfile.txt"

columns = 40
rows = 40

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
            if 0 <= nx < grid.columns and 0 <= ny < grid.rows and grid.cellgrid[nx][ny].alive:
                neighbors += 1
        return neighbors

class Grid:
    """Defines a grid of cells in a generation."""
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cellgrid = Array2D([[Cell(x, y, False) for y in range(rows)] for x in range(columns)],)

    def update_grid(self):
        """Creates a new Grid object for the next generation."""
        new_cellgrid = Grid(rows = self.rows, columns = self.columns)
        new_cellgrid.cellgrid = [[Cell(x, y, False) for y in range(self.rows)] for x in range(self.columns)]
        for x in range(self.columns):
            for y in range(self.rows):
                cell = self.cellgrid[x][y] 
                neighbors = cell.detect_neighbors(self)
                next_alive = (neighbors == 3) or (cell.alive and neighbors in [2, 3])
                new_cellgrid.cellgrid[x][y].alive = next_alive
        return new_cellgrid

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
        self.generation = 0
        self.gridcols = int(rows)
        self.gridrows = int(columns)
        self.kb = KBHit()
        self.choose_mode()
        self.grid = self.start_colony()
        self.run_game()

    def choose_mode(self):
        """Allows user to choose between automatic or manual mode, as well as quitting."""
        while True:
            response = input("Welcome to the Game of Life! (A)utomatic, (M)anual, or (Q)uit? \n").strip().upper()
            if response in ["A", "M", "Q"]:
                self.mode = "Automatic" if response == "A" else "Manual" if response == "M" else exit()
                self.speed = 1 if self.mode == "Automatic" else 0
                break
            print("Invalid input. Type 'A', 'M', or 'Q'.")
        if self.mode == "Automatic":
            while True:
                response = input("What speed would you to simulate at? (F)ast, (M)edium, or (S)low? \n").strip().upper()
                if response == "F": 
                    self.speed = 1
                    break
                elif response == "M": 
                    self.speed = 3
                    break
                elif response == "S": 
                    self.speed = 5
                    break
                else: print("Invalid response. Please choose a speed.") 

    def start_colony(self):
        """Creates a starting grid based on the inputed file or randomly."""
        response = input("Would you like a (R)andom start or (F)ile input? \n").strip().upper()
        print(" ")
        if response == "R":
            self.gridrows = rows
            self.gridcols = columns
            grid = Grid(self.gridrows, self.gridcols)
            for x in range(grid.columns):
                for y in range(grid.rows):
                    grid.cellgrid[x][y].alive = random.choice([True, False])  
            return grid
        elif response == "F":
            filename = importedfile
            try:
                with open(filename, 'r') as file:
                    lines = [line.rstrip() for line in file if line.strip()]  
                file_rows = len(lines)
                file_columns = max(len(line) for line in lines) 
                self.gridrows = file_rows
                self.gridcols = file_columns
                grid = Grid(self.gridrows, self.gridcols) 
                for y, line in enumerate(lines):
                    for x, char in enumerate(line):
                        if char == 'O': 
                            grid.cellgrid[x][y].alive = True
                return grid
            except FileNotFoundError:
                print("File not found. Please select again. \n")
                return self.start_colony()
        else:
            print("Invalid choice. Please select (R)andom or (F)ile. \n")
            return self.start_colony()


    def run_game(self):
        """Runs the game and deals with grid history."""
        while True:
            self.history.append(copy.deepcopy(self.grid))
            if len(self.history) > 5:
                self.history.pop(0)
            self.display_grid()
            if self.check_stability():
                print(self.endmessage)
                break
            self.grid = self.next_generation()
            if self.mode == "Manual":
                self.wait_for_manual_input()
            else:
                time.sleep(self.speed)

    def display_grid(self):
        """Prints the current generation."""
        print(f"Generation {self.generation}")
        self.generation += 1
        for y in range(self.gridrows):
            for x in range(self.gridcols):
                cell = self.grid.cellgrid[x][y]
                print("🦠" if cell.alive else " ‎ ", end="")
            print()

    def check_stability(self):
        """Checks if the grid has become stable or is repeating."""
        if not any(cell.alive for x in range(self.grid.columns) for y in range(self.grid.rows) 
            if (cell := self.history[-1].cellgrid[x][y])):
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

    def next_generation(self):
        """Creates the next generation and returns it."""
        return self.grid.update_grid()

    def wait_for_manual_input(self):
        """Handles manual stepping through generations."""
        print("Press 'N' for next, 'A' for automatic, 'Q' to quit. \n")
        while True:
            while not self.kb.kbhit():
                time.sleep(0.1)  
            key = self.kb.getch().lower()
            if key == 'q':
                exit()
            elif key == 'a':
                self.mode = "Automatic"
                print("Switched to Automatic mode. \n")
                return  
            elif key == 'n':
                return  
            else:
                print("Invalid key. Use 'N' to step, 'A' for auto, 'Q' to quit. \n")

if __name__ == "__main__":
    GameController()

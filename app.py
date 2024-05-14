import random

from grid import Grid
from position import Position

def input_grid(grid):
    for square in grid.iterate():
        
        square.highlight = True
        print(grid)
        square.highlight = False

        loop_condition = True
        while loop_condition:
            print("Enter value:")
            value = int(input())
            loop_condition = not square.set_value(value)

def main():
    grid = Grid(3,3)
    input_grid(grid)
    

if __name__ == "__main__":
    main()
from grid import Grid
from solve import solve

def input_grid(grid):
    for square in grid.squares:

        square.highlight = True
        print(grid)
        square.highlight = False

        loop_condition = True
        while loop_condition:
            print("Enter value:")
            value = int(input())
            loop_condition = not square.set_value(value)

def main():
    grid = Grid(3, 2)
    input_grid(grid)
    solve(grid)

if __name__ == "__main__":
    main()
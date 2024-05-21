from grid import Grid
from solve import solve

def input_grid(grid):
    for square in grid.squares:
        print_grid(grid, square)
        while True:
            print("Enter value:")
            value = int(input())
            try:
                square.set_value(value)
            except ValueNotPossibleException:
                continue
            break

def print_grid(grid, highlighted_square):
    highlighted_square.highlight = True
    print(grid)
    highlighted_square.highlight = False

def main():
    grid = Grid(3, 3)
    input_grid(grid)

    print(grid)
    print("Solving...")
    solve(grid)
    print(grid)

if __name__ == "__main__":
    main()
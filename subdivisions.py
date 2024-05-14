class Subdivision:
    def generator(self):
        length = self.grid.length
        return (self.squares[i] for i in range(length))


class Row(Subdivision):
    def __init__(self, grid, index):
        self.grid = grid
        self.squares = grid.squares[index]


class Column(Subdivision):
    def __init__(self, grid, index):
        self.grid = grid
        self.squares = [grid.squares[row][index] for row in range(grid.length)]


class Box(Subdivision):
    def __init__(self, grid, index):
        self.grid = grid
        self.squares = []

        box_width, box_height = grid.box_width, grid.box_height

        # row / column relative to other boxes
        box_row = index // box_height
        box_column = index % box_height

        # row / column of starting square
        starting_row = box_row * box_height
        starting_column = box_column * box_width

        for i in range(grid.length):
            square_row = starting_row + (i // box_width)
            square_column = starting_column + (i % box_width)
            square = grid.squares[square_row][square_column]
            self.squares.append(square)
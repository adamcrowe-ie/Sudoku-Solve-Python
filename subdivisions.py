class Subdivision:
    def generator(self):
        length = self.grid.length
        return (self.squares[i] for i in self.grid.range())


class Row(Subdivision):
    def __init__(self, grid, row):
        self.grid = grid
        self.squares = [ grid.squares[ grid.to_index(row, column) ] for column in grid.range()]


class Column(Subdivision):
    def __init__(self, grid, column):
        self.grid = grid
        self.squares = [ grid.squares[ grid.to_index(row, column) ] for row in grid.range()]


class Box(Subdivision):
    def __init__(self, grid, box):
        self.grid = grid
        self.squares = []

        box_w, box_h = grid.box_width, grid.box_height

        box_row = box // box_h
        box_column = box % box_h
        starting_row = box_row * box_h
        starting_column = box_column * box_w
        starting_index = grid.to_index(starting_row, starting_column)

        for i in grid.range():
            index = starting_index + grid.to_index(i // box_w, i % box_w)
            square = grid.squares[index]
            self.squares.append(square)
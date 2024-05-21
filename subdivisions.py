from position import Position

class Subdivision:
    def get_empty_squares(self):
        return {square for square in self.squares if not square.value}
    
    def __repr__(self):
        return f"{self.type} {self.index + 1}"

class Row(Subdivision):
    def __init__(self, row):
        self.checked = False
        self.type = "Row"
        self.index = row
        self.squares = []

        grid = self.grid
        for column in grid.range():
            index = Position(row, column).index
            square = grid.squares[index]
            self.squares.append(square)


class Column(Subdivision):
    def __init__(self, column):
        self.checked = False
        self.type = "Column"
        self.index = column
        self.squares = []

        grid = self.grid
        for row in grid.range():
            index = Position(row, column).index
            square = grid.squares[index]
            self.squares.append(square)

class Box(Subdivision):
    def __init__(self, box):
        self.checked = False
        self.type = "Box"
        self.index = box
        self.squares = []
        
        grid = self.grid
        box_width, box_height = grid.box_width, grid.box_height

        box_row = box // box_height
        box_column = box % box_height
        starting_row = box_row * box_height
        starting_column = box_column * box_width
        starting_index = Position(starting_row, starting_column).index

        for i in grid.range():
            iterated_row = i // box_width
            iterated_column = i % box_width
            iterated_index =  Position(iterated_row, iterated_column).index

            index = starting_index + iterated_index
            square = grid.squares[index]
            self.squares.append(square)
from position import Position
from square import Square
from subdivisions import Row, Column, Box

class Grid:
    def __init__(self, box_width, box_height):
        # box_width & box_height determine the width/height of the boxes that subdivide the grid
        self.box_width, self.box_height = box_width, box_height
        self.length = box_width * box_height

        self.to_index = lambda row, column: (row * self.length) + column

        self.squares = []
        for i in self.range():
            for j in self.range():
                position = Position(self, i, j)
                square = Square(self, position)
                self.squares.append(square)

        self.rows = [Row(self, i) for i in self.range()]
        self.columns = [Column(self, i) for i in self.range()]
        self.boxes = [Box(self, i) for i in self.range()]

    def range(self):
        for i in range(self.length):
            yield i

    # acts as a way to print out our grid
    def __str__(self):
        string = "\n"  # our string we return

        for square in self.squares:
            row, column = square.position.row, square.position.column

            if row != 0 and column == 0:
                string += "\n\n" if row % self.box_height == 0 else "\n"

            string += "   " if column % self.box_width == 0 else " "
            
            if square.highlight:
                string += "X"
            else:
                string += str(square.value) if square.value != 0 else "\u2610"
                 
        string += "\n"
        return string
from position import Position
from square import Square
from subdivisions import Subdivision, Row, Column, Box

class Grid:
    def __init__(self, box_width, box_height):
        # box_width & box_height determine the width/height of the boxes that subdivide the grid
        self.box_width, self.box_height = box_width, box_height
        Position.box_width, Position.box_height = box_width, box_height

        self.length = box_width * box_height
        self.empty_squares = self.length**2

        Square.grid = self
        self.squares = []
        for i in self.range():
            for j in self.range():
                position = Position(i, j)
                square = Square(position)
                self.squares.append(square)

        Subdivision.grid = self
        self.rows = [Row(i) for i in self.range()]
        self.columns = [Column(i) for i in self.range()]
        self.boxes = [Box(i) for i in self.range()]
        self.subdivisions = self.rows + self.columns + self.boxes

    def range(self):
        for i in range(self.length):
            yield i

    def check_solved(self):
        for square in self.squares:
            if not square.value:
                return False
        return True

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
            elif square.value != 0:
                string += str(square.value)
            elif square.locked:
                string += "L"
            else:
                string += "\u2610"
                 
        string += "\n"
        return string
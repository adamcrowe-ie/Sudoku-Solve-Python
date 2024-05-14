from position import Position
from square import Square

class Grid:
    def __init__(self, box_width, box_height):
        # box_width & box_height determine the width/height of the boxes that subdivide the grid
        self.box_width, self.box_height = box_width, box_height
        self.length = box_width * box_height
        self.size = self.length ** 2 

        self._counter = 0  # counter for our iterator
        self.squares = [[] for i in range(self.length)]
        
        for i in range(self.length):
            for j in range(self.length):
                position = Position(i, j)
                square = Square(self, position)
                self.squares[i].append(square)

    def iterate(self):
        for i in range(self.length):
            for j in range(self.length):
                yield self.squares[i][j]

    # acts as a way to print out our grid
    def __str__(self):
        string = "\n"  # our string we return

        for square in self.iterate():
            x, y = square.position

            if x != 0 and y == 0:
                string += "\n\n" if x % self.box_height == 0 else "\n"

            string += "   " if y % self.box_width == 0 else " "
            string += str(square.value) if square.value != 0 else "\u2610"
                 
        string += "\n"
        return string
from collections import namedtuple

Square = namedtuple("Square", ["value", "possible_values"])

class Grid:
    def __init__(self, box_width, box_height):
        # box_width & box_height determine the width/height of the boxes that subdivide the grid
        self._box_width, self._box_height = box_width, box_height
        self._length = box_width * box_height

        self._counter = 0  # for iterator
        
        # square template - value is zero, and can take any value from 1 to L
        square = Square(0, [True]*self._length)

        # initialise grid as 2D list
        row = [square for i in range(self._length)]
        self._grid = [row for i in range(self._length)]
    
    def __iter__(self):
        self._counter = 0
        return self
    
    def __next__(self):
        if self._counter < self._length ** 2:
            x = self._counter // self._length
            y = self._counter % self._length
            
            self._counter += 1

            return (x, y, self._grid[x][y])
        else:
            raise StopIteration

    # acts as a way to print out our grid
    def __str__(self):
        string = "\n"  # our string we return

        for i, j, square in self:
            if i != 0 and j == 0:
                string += "\n\n" if i % self._box_height == 0 else "\n"
            string += "   " if j % self._box_width == 0 else " "
            string += str(square.value) if square.value != 0 else "\u2610"
                 
        string += "\n"
        return string
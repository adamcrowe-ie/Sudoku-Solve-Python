from position import Position

class Square:
    def __init__(self, grid, position):
        self.grid = grid
        self.position = position
        self.value = 0
        self.possible_values = [(i+1) for i in range(grid.length)]

    def set_value(self, value):
        if value == 0:
            return True
        elif value in self.possible_values:
            self.value = value
            self.possible_values = []

            for cosquare in self.subdivisions():
                if value in cosquare.possible_values:
                    cosquare.possible_values.remove(value)
            
            return True
        
        return False

    def row(self):
        y = self.position.y
        for i in range(self.grid.length):
            yield (self.grid.squares[i][y])

    def column(self):
        x  = self.position.x
        for i in range(self.grid.length):
            yield self.grid.squares[x][i]

    def box(self):
        x, y = self.position
        box_width, box_height = self.grid.box_width, self.grid.box_height

        box_x = (x // box_width) * box_width
        box_y = (y // box_height) * box_height

        for i in range(self.grid.length):
            yield self.grid.squares[box_x + (i % box_width)][box_y + (i // box_width)]

    def subdivisions(self):
        yield from self.row()
        yield from self.column()
        yield from self.box()
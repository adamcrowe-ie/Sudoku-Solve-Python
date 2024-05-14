from position import Position

class Square:
    def __init__(self, grid, position):
        self.grid = grid
        self.position = position
        self.value = 0
        self.possible_values = [(i+1) for i in range(grid.length)]
        self.highlight = False

    def set_value(self, value, update_possibilities=True):
        if value == 0:
            return True
        elif value in self.possible_values:
            self.value = value
            self.possible_values = []

            if update_possibilities:
                for square in self.subdivisions():
                    if value in square.possible_values:
                        square.possible_values.remove(value)
            return True
        return False

    def subdivisions(self):
        grid = self.grid
        row = self.position.row
        column = self.position.column 
        box = self.position.box

        yield from grid.rows[row].generator()
        yield from grid.columns[column].generator()
        yield from grid.boxes[box].generator()
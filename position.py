class Position:
    def __init__(self, grid, row, column):
        self.row, self.column = row, column

        box_width, box_height = grid.box_width, grid.box_height

        box_row = row // box_height
        box_column = column // box_width

        self.box = (box_row * box_height) + box_column
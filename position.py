class Position:
    def __init__(self, *args):
        box_width, box_height = self.box_width, self.box_height
        grid_length = box_width * box_height

        
        if len(args) == 1:              # if position defined from index
            self.index = args[0]
            self.row = self.index // grid_length
            self.column = self.index % grid_length
        else:                           # if position defined from row-column pair
            self.row, self.column = args
            self.index = (self.row * grid_length) + self.column
        
        box_row = self.row // box_height
        box_column = self.column // box_width

        self.box = (box_row * box_height) + box_column
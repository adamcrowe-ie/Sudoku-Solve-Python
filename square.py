from position import Position

class Square:
    def __init__(self, position):
        self.position = position
        self.value = 0
        self.possible_values = {(i+1) for i in self.grid.range()}
        self.highlight = False
        self.locked = False

    def set_value(self, value):
        if value == 0:
            return
        elif not value in self.possible_values:
            raise ValueNotPossibleException
        
        self.value = value
        self.possible_values = []
        self.grid.empty_squares -= 1

        for subdivision in self.get_subdivisions():
            for square in subdivision.get_empty_squares():
                if square.possible_values - {value} == set():
                    raise ValueNotPossibleException
                square.possible_values -= {value}
                
    
    def get_row(self):
        return self.grid.rows[self.position.row]
    
    def get_column(self):
        return self.grid.columns[self.position.column]
    
    def get_box(self):
        return self.grid.boxes[self.position.box]
    
    def get_subdivisions(self):
        return [self.get_row(), self.get_column(), self.get_box()]
    
    def __repr__(self):
        return f"({self.position.row + 1}, {self.position.column + 1})"
    
class ValueNotPossibleException(Exception):
    pass
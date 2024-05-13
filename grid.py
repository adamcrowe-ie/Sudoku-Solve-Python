class Grid:
    def __init__(self, box_width, box_height):
        self._box_width, self._box_height = box_width, box_height
        self._length = box_width * box_height
        
        # initialise grid as 2D list
        square = {"value": 0}
        row = [square for i in range(self._length)]
        self._grid = [row for i in range(self._length)]
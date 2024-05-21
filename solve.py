import copy
from grid import Grid
from square import ValueNotPossibleException

# 6 methods
# 1. Single candidate cells
# 2. Only possible value within subdivision
# 3. Locked cells type I
# 4. Locked cells type II
# 5. Directional elimination
# 6. Guess Values

def solve(grid):
    while (not grid.check_solved() and 
        (find_single_candidate_squares(grid)
        or find_unique_possibility_in_subdivisions(grid)
        or find_typeI_locked_squares(grid)
        or find_typeII_locked_squares(grid)
        or directional_elimination(grid)
        or guess_values(grid))):
        pass

def find_single_candidate_squares(grid):
    for square in grid.squares:
        if not square.value and len(square.possible_values) == 1:
            value = min(square.possible_values)
            square.set_value(value)
            return True
    return False
        
def find_unique_possibility_in_subdivisions(grid):
    for subdivision in grid.subdivisions:
        empty_squares = subdivision.get_empty_squares()
        
        squares_by_value = [[sq for sq in empty_squares if (i+1) in sq.possible_values] for i in grid.range()]
        for value, squares in enumerate(squares_by_value, 1):
            if len(squares) == 1:
                square = squares[0]
                square.set_value(value)
                return True
    return False

def find_typeI_locked_squares(grid):
    for subdivision in grid.subdivisions:
        empty_squares = subdivision.get_empty_squares()
        seen = set()

        for square in empty_squares:
            possible_values = square.possible_values
            if square in seen:
                continue

            matching_squares = {sq for sq in empty_squares if sq.possible_values == possible_values}
            seen = seen | matching_squares
            
            if len(matching_squares) != len(possible_values):
                continue
            
            shared_squares = find_shared_squares(matching_squares)
            change = False

            for new_square in shared_squares:
                if new_square in matching_squares:
                    continue
                change = change or bool(new_square.possible_values & possible_values)
                new_square.possible_values -= possible_values

            if change:
                return True
    return False

def find_typeII_locked_squares(grid):
    for subdivision in grid.subdivisions:
        empty_squares = subdivision.get_empty_squares()
        
        squares_by_value = [[sq for sq in empty_squares if (i+1) in sq.possible_values] for i in grid.range()]
        seen = set()

        for value, squares in enumerate(squares_by_value, 1):
            if not squares or value in seen:
                continue
            matching_values = {val for val, sqs in enumerate(squares_by_value, 1) if sqs == squares}
            seen = seen | matching_values

            if len(matching_values) != len(squares):
                continue
            
            shared_squares = find_shared_squares(squares)
            change = False

            for new_square in shared_squares:
                if new_square in squares:
                    change = change or bool(new_square.possible_values - matching_values)
                    new_square.possible_values = copy.deepcopy(matching_values)
                    continue
                change = change or bool(new_square.possible_values & matching_values)
                new_square.possible_values -= matching_values

            if change:
                return True

def directional_elimination(grid):
    for box in grid.boxes:
        empty_squares = box.get_empty_squares()
        squares_by_value = [[sq for sq in empty_squares if (i+1) in sq.possible_values] for i in grid.range()]

        for value, squares in enumerate(squares_by_value, 1):
            if not len(squares) in {2, 3}:
                continue
            
            shared_subdivision = None
            rows = {sq.position.row for sq in squares}
            columns = {sq.position.column for sq in squares}
            
            if len(rows) == 1:
                shared_subdivision = grid.rows[min(rows)]
            elif len(columns) == 1:
                shared_subdivision = grid.columns[min(columns)]
            else:
                continue
            
            change = False

            for square in shared_subdivision.get_empty_squares():
                if square in squares:
                    continue
                change = change or bool(value in square.possible_values)
                square.possible_values -= {value}
            
            if change:
                return True
    return False

def guess_values(grid):
    # find square with least number of possibilities
    square = None
    for i in grid.range():
        if i < 2:
            continue
        
        square = next((sq for sq in grid.squares if len(sq.possible_values) == i), None)
        if square:
            break

    possible_values = copy.deepcopy(square.possible_values)
    for value in possible_values:
        new_grid = Grid(grid.box_width, grid.box_height)
        
        for i, sq in enumerate(new_grid.squares):
            sq.set_value(grid.squares[i].value)

        try:
            index = square.position.index
            new_grid.squares[index].set_value(value)
            solve(new_grid)
        except ValueNotPossibleException:
            continue
        else:
            for i, sq in enumerate(grid.squares):
                if not sq.value:
                    sq.set_value(new_grid.squares[i].value)
            return True


def find_shared_squares(squares):
    shared_squares = set()

    if squares:
        first_square = list(squares)[0]
        grid = first_square.grid
        row = first_square.position.row
        column = first_square.position.column
        box = first_square.position.box

        if all((sq.position.row == row) for sq in squares):
            shared_squares = shared_squares | grid.rows[row].get_empty_squares()

        if all((sq.position.column == column) for sq in squares):
            shared_squares = shared_squares | grid.columns[column].get_empty_squares()

        if all((sq.position.box == box) for sq in squares):
            shared_squares = shared_squares | grid.boxes[box].get_empty_squares()

    return shared_squares
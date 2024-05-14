# When we assign a value to a square, this is likely to determine the value of another square in the same
# row / col / box. Therefore, our algorithm for sake of efficiency, should check along these subdivisions

# The ways we can determine cell values:
#    1. There is only one possible value
#    2. It is the unique square in a row / col / box that can take a value
#    3. Guessing
# We can also eliminate the number of possible values a square can have by finding "locked" squares in the 
# same subdivision

# Method:
# 1. Check square -- if no changes check another -- if check 

def solve(grid):
    pass
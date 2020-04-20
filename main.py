import numpy as np
import puzzle

board = puzzle.get_puzzle()

print('Problem: ')
print(board)

# a mask that is used to retain info about
# which values were an original part of the problem
editable = (board == 0)

def is_safe_to_insert(n, i, j, board):
    # checking rows and cols
    if n in board[i, :] or n in board[:, j]:
        return False
    
    # checking its corresponding 3x3 block
    # e.g. if i=2, j=8
    # board[0:3, 6:9] will be checked
    row_start, col_start = 3 * (i // 3), 3 * (j // 3)
    if n in board[row_start : row_start + 3, col_start : col_start + 3]:
        return False
    
    return True

# init spot number on the board
spot = 0
moving_backwards = False

# iterate until we reach the end of board
while spot < 81:

    # convert to row and column index
    r, c = spot // 9, spot % 9
    
    # check if the spot was filled as part of the problem
    if not editable[r, c]:
        # move either front or back according to the flag
        spot += -1 if moving_backwards else 1
        continue
    
    # clone the value, increment and test
    num = board[r, c]
    num += 1

    # try values up to 9 that satisfy sudoku conditions
    while not is_safe_to_insert(num, r, c, board) and num < 10:
        num += 1
        
    if num == 10:
        # means none of the numbers are working
        # reset value at that spot
        board[r, c] = 0
        
        # time to back track, go back one spot
        spot -= 1

        # set the backwards flag so that
        # the 'editable' check knows we're backtracking
        moving_backwards = True
        continue
        
    # value of num satifies conditions
    board[r, c] = num

    # move on to the next spot
    spot += 1
    
    # unset the backwards flag
    moving_backwards = False

print('\nSolution: ')
print(board)


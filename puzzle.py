import numpy as np

def get_puzzle():

    # read puzzle from file
    puzzle = open('puzzle.txt')
    contents = puzzle.readlines()
    puzzle.close()
    
    # remove new line char and cast to np.ndarray
    board = [list(line.replace('\n', '')) for line in contents]
    board = np.array(board, dtype=np.int16)
    
    return board

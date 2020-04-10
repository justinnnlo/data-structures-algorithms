''' 9 x 9 sudoku board '''


def is_valid_sudoku(board):
    seen = []

    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c != '.':
                seen += [(c, j), (i, c), (i/3, j/3, c)]
    return len(seen) == len(set(seen))

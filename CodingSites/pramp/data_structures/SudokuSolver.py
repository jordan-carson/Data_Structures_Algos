# # 5 3 _ | _ 7 _ _ _ _
# # 6 _ _ |1 9 5 _ _ _
# # _ 9 8 |_ _ _ _ 6 _
# # 8 _ _ _ 6 _ _ _ 3
# # 4 _ _ 8 _ 3 _ _ 1
#
#
# def findNext(board):
#     possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for row in board:
#         for col in board:
#             if board[row][col] not in possible_values:
#                 getCandidates(board, board[row], board[col])
#             return None
#
#
# def getCandidates(board, row, col):
#     # What values can be placed in empty cell board[row][col] ?
#     candidates = []
#     # For each character add it to the candidate list
#     # only if there's no collision, i.e. that character
#     # doesn't already exist in the same row, column
#     # and sub-board. Notice the top-left corner of (row, col)'s
#     # sub-board is (row - row%3, col - col%3)
#     sub_board = set()
#     isCollision = False
#     isEmpty = False
#     candidates = []
#     for i in range(0, 9):
#         for j in range(0, 9):
#             if board[i][j] not in sub_board:
#
#         if not isCollision:
#             candidates.append(char)
#
#     return candidates

    # not in the first 3x3  = > 1 2 4 7

    # if board[row][col] not in sub_board:
    #  sub_board.add(board[row][col])
# pass  # your code goes here


from math import floor
def getCandidates(board, row, col):
    # For some empty cell board[row][col], what possible
    # characters can be placed into this cell
    # that aren't already placed in the same row,
    # column, and sub-board?

    # At the beginning, we don't have any candidates
    candidates = []

    # For each character add it to the candidate list
    # only if there's no collision, i.e. that character
    # doesn't already exist in the same row, column
    # and sub-board. Notice the top-left corner of (row, col)'s
    # sub-board is (row - row%3, col - col%3).
    # for chr from '1' to '9':
    for chr in board:
        collision = False
        for i in range(0, 9):
            if (board[row][i] == chr or
                    board[i][col] == chr or
                    board[(row - row % 3) + floor(i / 3)][(col - col % 3) + i % 3] == chr):
                collision = True
                break

        if not collision:
            candidates.append(chr)

    return candidates


def sudokuSolve(board):
    # For each empty cell, consider 'newCandidates', the
    # set of possible candidate values that can
    # be placed into that cell.

    row = -1
    col = -1
    candidates = None

    for r in range(0, 9):
        for c in range(0, 9):
            if board[r][c] == '.':
                newCandidates = getCandidates(board, r, c)
                # Then, we want to keep the smallest
                # sized 'newCandidates', plus remember the
                # position where it was found
                if candidates is None or len(newCandidates) < len(candidates):
                    candidates = newCandidates
                    row = r
                    col = c

    # If we have not found any empty cell, then
    # the whole board is filled already
    if candidates is None:
        return True

    # For each possible value that can be placed
    # in position (row, col), let's
    # place that value and then recursively query
    # whether the board can be solved.  If it can,
    # we are done.
    for val in candidates:
        board[row][col] = val
        if sudokuSolve(board):
            return True
        # The tried value val didn't work so restore
        # the (row, col) cell back to '.'
        board[row][col] = '.'

    # Otherwise, there is no value that can be placed
    # into position (row, col) to make the
    # board solved
    return False



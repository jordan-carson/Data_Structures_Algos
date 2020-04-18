def valid_tries(current_tries, row, col, board):
    for ele in board[row]:
        if ele != '.' and ele in current_tries:
            current_tries.remove(ele)
        for ele in board[col]:
            if ele != '.' and ele in current_tries:
                current_tries.remove(ele)
        for i in range(row // 3, 3 + row // 3):
            for j in range(col // 3, 3 + col // 3):
                if board[i][j] != '.' and board[i][j] in current_tries:
                    current_tries.remove(board[i][j])
    return current_tries


def sudoku_solve(board):
    found = False
    for col in range(len(board[0])):
        for row in range(len(board)):
            if board[row][col] == '.':
                found = True
                current_tries = [i + 1 for i in range(9)]
                current_tries = valid_tries(current_tries, row, col, board)
                while len(current_tries) > 0:
                    board[row][col] = current_tries.pop()
                    if sudoku_solve(board) == True:
                        return True
                return False




test_case = [[".","8","9",".","4",".","6",".","5"],[".","7",".",".",".","8",".","4","1"],["5","6",".","9",".",".",".",".","8"],[".",".",".","7",".","5",".","9","."],[".","9",".","4",".","1",".","5","."],[".","3",".","9",".","6",".","1","."],["8",".",".",".",".",".",".",".","7"],[".","2",".","8",".",".",".","6","."],[".",".","6",".","7",".",".","8","."]]


print(sudoku_solve(test_case))
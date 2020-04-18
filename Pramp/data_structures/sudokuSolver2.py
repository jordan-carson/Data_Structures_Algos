# # include <iostream>
# # include <vector>
#
# using
# namespace
# std;
# / *
# 1
# st
# step
# check
# the
# board is valid(checking
# each
# row and column and box
# for dups)
# 2
# nd = > checking
# for each missing number in each row and column
#
# rowCheck(r, val)
#
# columnCheck(c, val)
#
# boxCheck(r)
#
# for (i:0 to 9)
#     for (j : 0 to 9)
#         if (cell == '.')
#             for i = 1 to 9 {
#             if (rowCheck() & & columnCheck()){
#             cell = num
#             if (solve())
#             return true;
#             call = '.'
#         }
#         }
#
#         return false
# * /
#
# bool
# rowCheck(int
# r, int
# val_cl, char
# val, vector < vector < char >> & board){
# for (int i = 0;i < 9;i++){
# if (i != val_cl & & board[r][i] == val)
#     return false;
# }
#
# return true;
# }
#
# bool
# columnCheck(int
# c, int
# val_r, char
# val, vector < vector < char >> & board){
# for (int i = 0;i < 9;i++){
# if (i != val_r & & board[i][c] == val)
#     return false;
# }
#
# return true;
# }
#
# int
# getStart(int
# x){
# return x < 3 ? 0: x < 6 ? 3: 6;
# }
#
# bool
# boxCheck(int
# r, int
# c, char
# val, vector < vector < char >> & board){
# int
# stR = getStart(r), stC = getStart(c);
# for (int  i = stR;i < stR+3;i++)
#     for (int j = stC;j < stC+3;j++)
#         if (i != r & & j != c & & board[i][j] == val)
#             return false;
#
# return true;
# }
#
# bool
# sudokuSolver(vector < vector < char >> & board)
# {
# bool
# completed = true;
#
# // your
# code
# goes
# here
# for (int x = 0; x < 9;x++){
# for (int y = 0;y < 9;y++){
# if (board[x][y] == '.'){
# completed = false;
# for (int v = 1;v <= 9;v++){
# char val = ('0'+v);
# if (rowCheck(x, y, val, board) & & columnCheck(y, x, val, board) & & boxCheck(x, y, val, board)){
# board[x][y] = val;
# if (sudokuSolver(board))
# return true;
# board[x][y] = '.';
# }
# }
# }
# }
# }
#
# return completed;
# }
#
# bool
# sudokuSolve(const
# vector < vector < char >> & b ) {
# vector < vector < char >> board = b;
#
# bool
# completed = true;
# for (int i = 0;i < 9;i++)
#     for (int j = 0;j < 9;j++){
#         completed&= (board[i][j] != '.');
#     if (board[i][j] != '.' & & !(rowCheck(i, j, board[i][j], board) & & columnCheck(j, i, board[i][j], board) & & boxCheck(i, j, board[i][j], board)))
#     return false;
#     }
#
#     return true; // completed ? true: sudokuSolver(board);
# }
#
# int
# main()
# {
# return 0;
# }
#
# //  # A helper function that returns a set of all valid
# //  # candidates for a given cell in the board
#
# // function
# getCandidates(board, row, col):
# //  # For some empty cell board[row][col], what possible
# //  # characters can be placed into this cell
# //  # that aren't already placed in the same row,
# //  # column, and sub-board?
#
# //  # At the beginning, we don't have any candidates
# // candidates = []
#
#                 //  # For each character add it to the candidate list
#                 //  # only if there's no collision, i.e. that character
#                 //  # doesn't already exist in the same row, column
#                 //  # and sub-board. Notice the top-left corner of (row, col)'s
#                 //  # sub-board is (row - row%3, col - col%3).
#                 //
# for chr from '1' to '9':
#     //
# collision = false;
# // for i from 0 to 8:
#     //
# if (table[row][i] == chr | |
#     // table[i][col] == chr | |
# // table[(row - row % 3) + floor(i / 3)][(col - col % 3) + i % 3] //== chr):
# // collision = true
#                //
# break
# //
# // if (!collision):
#     // candidates.push(chr)
# //
# // return candidates


def sudoku_solve(board):
    square_set = [[set() for j in range(3)] for i in range(3)]
    row_set = [set() for j in range(9)]
    col_set = [set() for j in range(9)]

    # ignore all the '.', add everything else
    for irow in range(3):
        row = board[irow]
        for icol in range(3):
            val = row[icol]

            if val == '.': continue
            if val in row_set[irow%3]: return False
            if val in col_set[icol%3]: return False
            if val in square_set[irow%3][icol%3]: return False

            row_set[irow].add(val)
            col_set[icol].add(val)
            square_set[irow][icol].add(val)

    return True


test_board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],

    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],

    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

print(sudoku_solve(test_board))
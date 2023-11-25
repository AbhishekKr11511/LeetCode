'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

# Solution
# Time complexity = O(n^2) + O(n^2) + O(n^2) where n is 9 since sudoku is 9x9 
# Time complexity = O(n^2)
# ---------------------------

def checkRows(input):
    result = True
    for i in range(9):
        count = {}
        for n in input[i]:
            if n==".":
                continue
            count[n] = 1 + count.get(n, 0)
        result = result and all(x<=1 for x in list(count.values()))
    return result

def checkColumns(input):
    result = True
    for i in range(9):
        count = {}
        for j in range(9):
            if input[j][i]==".":
                continue
            count[input[j][i]] = 1 + count.get(input[j][i], 0)
        result = result and all(x<=1 for x in list(count.values()))
    return result

def checkGrid(input):
    result = True
    for i in range(0,9,3):
        for j in range(0,9,3):
            count = {}
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if input[x][y] == ".":
                        continue
                    count[input[x][y]] = 1 + count.get(input[x][y],0)
            result = result and all(z<=1 for z in count.values())
    return result


def isValidSudoku(board):
    return checkRows(board) and checkColumns(board) and checkGrid(board)



print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Example 1:

# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true
# Example 2:

# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false
# Explanation: There are two 1's in the top-left 3x3 sub-box.

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
-----------------------------------------------------------------------------------------------------------------------------------
#Driver Code
board = [["1","2",".",".","1",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(solve(board))
-----------------------------------------------------------------------------------------------------------------------------------
Approach 1:
-----------------------------------------------------------------------------------------------------------------------------------
def solve(board ):
    #check row wise
    for i in range(len(board)):
        numbers = set()
        for j in range(len(board)):
            if board[i][j] == '.':
                continue
            elif board[i][j] in numbers:
                return False
            numbers.add(board[i][j])
    #check column wise
    for j in range(len(board)):
        numbers = set()
        for i in range(len(board)):
            if board[i][j] == '.':
                continue
            elif board[i][j] in numbers:
                return False
            else :
                numbers.add(board[i][j])
    #check 3*3 wise
    for row_start in range(0, 9, 3):
        for col_start in range(0,9,3):
            numbers = set()
            for i in range(row_start, row_start+3):
                for j in range(col_start, col_start+3):
                    if board[i][j] == '.':
                        continue
                    elif board[i][j] in numbers:
                        return False
                    else :
                        numbers.add(board[i][j]) 
    return True
T.C : O(n^2)
S.C : O(n)

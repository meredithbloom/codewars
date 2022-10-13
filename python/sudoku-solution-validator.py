# Sudoku Solution Validator - 4 kyu
'''
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
'''
from collections import Counter

def valid_solution(board):
    rows = {}
    columns = {}
    boxes = {}
    
    
        
    
    
    
    for r in range(9):
        rows[r] = Counter(board[r])
        print(f'current row is row {r}, counter: {rows[r]}, list: {list(rows[r])}')
        if len(list(rows[r])) != 9:
            return False
        col = []
        for c in range(9):
            if board[c][r] == 0:
                return False
            col.append(board[c][r])   
        columns[r] = Counter(col)
        print(f'current col is col {r}, counter: {columns[r]}, list: {list(columns[r])}')
        print()
        if len(list(columns[r])) != 9:
            return False
    return True
        
    #print(rows)
    
    
    
# print(valid_solution([
#     [1, 2, 3, 4, 5, 6, 7, 8, 9], 
#     [2, 3, 4, 5, 6, 7, 8, 9, 1], 
#     [3, 4, 5, 6, 7, 8, 9, 1, 2], 
#     [4, 5, 6, 7, 8, 9, 1, 2, 3], 
#     [5, 6, 7, 8, 9, 1, 2, 3, 4], 
#     [6, 7, 8, 9, 1, 2, 3, 4, 5], 
#     [7, 8, 9, 1, 2, 3, 4, 5, 6], 
#     [8, 9, 1, 2, 3, 4, 5, 6, 7], 
#     [9, 1, 2, 3, 4, 5, 6, 7, 8]
# ])) # false



# print(valid_solution([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ])) # true

# print(valid_solution([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 6, 2, 4, 8, 5, 9],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ])) # false



# print(valid_solution([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 0, 3, 4, 8],
#     [1, 0, 0, 3, 4, 2, 5, 6, 0],
#     [8, 5, 9, 7, 6, 1, 0, 2, 0],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 0, 1, 5, 3, 7, 2, 1, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ])) # false

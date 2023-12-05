'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

def searchMatrix(matrix, target):
    startRow = 0
    startColumn = 0
    endRow = len(matrix)-1
    endColumn = len(matrix[0])-1
    mid = (startRow+endRow)//2
    while target >= matrix[startRow][startColumn] and target <= matrix[endRow][endColumn]:
        if startRow == endRow:
            break
        if target == matrix[mid][0]:
            return [mid, 0]
        elif target > matrix[mid][0]:
            if endRow-startRow == 1 and matrix[endRow][0] <= target:
                startRow = endRow
                continue
            elif endRow-startRow == 1 and matrix[endRow][0] > target:
                endRow = startRow
                continue
            startRow = mid
            mid = (startRow+endRow)//2
            continue
        elif target < matrix[mid][0]:
            if endRow-startRow==1:
                endRow = startRow
                continue
            endRow = mid
            mid = (startRow+endRow)//2
            continue
    
    targetArray = matrix[startRow]
    while target >= targetArray[startColumn] and target <= targetArray[endColumn]:
        if targetArray[(startColumn+endColumn)//2] == target:
            return [startRow, (startColumn+endColumn)//2]
        elif targetArray[(startColumn+endColumn)//2] < target:
            startColumn = (startColumn+endColumn)//2+1
            continue
        elif targetArray[(startColumn+endColumn)//2] > target:
            endColumn = (startColumn+endColumn)//2
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 8))
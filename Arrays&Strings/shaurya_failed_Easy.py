"""
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
def pascalsTriangle(numRows):
    newRow=[0] * numRows
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1,1]]
    else:
        oldRow = pascalsTriangle(numRows-1)[-1]
        
        newRow[0] = newRow[numRows-1] = 1
        for i in range(1, numRows-2):
            newRow[i] = oldRow[i-1] + oldRow[i]
        return pascalsTriangle(numRows-1).append(newRow)
def gameOfLife(matrix):
    """
    Given a board with m by n cells, each cell has an initial state live (1) or 
    dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, 
    diagonal). 

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    Write a function to compute the next state (after one update) of the board 
    given its current state. The next state is created by applying the above 
    rules simultaneously to every cell in the current state, where births and 
    deaths occur simultaneously.


    Idea: putting markers in different entries, and updating them later. 
    """

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count = checkLiveCount(matrix, i, j)
            if matrix[i][j] == 1:
                if count < 2:
                    matrix[i][j] = 'wa'
                elif count == 2 or count == 3:
                    continue
                elif count > 3:
                    matrix[i][j] = 'wa'
            elif count == 3:
                matrix[i][j] = 'wd'

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'wd':
                matrix[i][j] = 1
            elif matrix[i][j] == 'wa':
                matrix[i][j] = 0

    print(matrix)


def checkLiveCount(matrix, i, j):
    count = 0
    for m in range(-1, 2):
        for n in range(-1, 2):
            if m == 0 and n == 0:
                continue
            elif inBounds(matrix, i + m, j + n) and (matrix[i + m][j + n] == 1 or matrix[i + m][j+n] == 'wa'):
                count += 1

    return count


def inBounds(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

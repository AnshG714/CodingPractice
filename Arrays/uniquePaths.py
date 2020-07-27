def uniquePaths(m: int, n: int):
    """
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in 
    the diagram below).

    The robot can only move either down or right at any point in time. The robot 
    is trying to reach the bottom-right corner of the grid (marked 'Finish' 
    in the diagram below).

    How many possible unique paths are there?

    SOLUTION: DYNAMIC PROGRAMMING
    """
    memo = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        memo[i][0] = 1

    for i in range(n):
        memo[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

    return memo[-1][-1]

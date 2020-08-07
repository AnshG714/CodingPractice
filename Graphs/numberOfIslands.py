def numIslands(grid: [[str]]):
    """
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
    An island is surrounded by water and is formed by connecting adjacent lands 
    horizontally or vertically. You may assume all four edges of the grid are all 
    surrounded by water.

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3
    """
    visited = set()
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and (i, j) not in visited:
                count += 1
                dfs(grid, visited, i, j)

    return count


def dfs(grid, visited, i, j):
    visited.add((i, j))
    neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for neighbor in neighbors:
        nextI = i + neighbor[0]
        nextJ = j + neighbor[1]
        if inbounds(grid, nextI, nextJ) and grid[nextI][nextJ] == '1' and (nextI, nextJ) not in visited:
            dfs(grid, visited, nextI, nextJ)


def inbounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

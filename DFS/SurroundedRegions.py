def surroundedRegions(board):
    """
    Given a 2D board containing 'X' and 'O' (the letter O), capture all regions 
    surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.

    Example:

    X X X X
    X O O X
    X X O X
    X O X X

    After running your function, the board should be:

    X X X X
    X X X X
    X X X X
    X O X X

    Explanation:

    Surrounded regions shouldn’t be on the border, which means that any 'O' on the 
    border of the board are not flipped to 'X'. Any 'O' that is not on the border 
    and it is not connected to an 'O' on the border will be flipped to 'X'. Two 
    cells are connected if they are adjacent cells connected horizontally or 
    vertically.
    """
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(board), len(board[0])

    def dfs(i, j):
        board[i][j] = "S"
        for dx, dy in neighbors:
            if 0 <= i + dx < len(board) and 0 <= j + dy < len(board[0]) and board[i + dx][j + dy] == 'O':
                dfs(i + dx, j + dy)

    for i in range(cols):
        if board[0][i] == "O":
            dfs(0, i)
        if board[-1][i] == "O":
            dfs(rows - 1, i)

    for i in range(rows):
        if board[i][0] == "O":
            dfs(i, 0)
        if board[i][-1] == "O":
            dfs(i, cols - 1)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "S":
                board[i][j] = "O"
            else:
                board[i][j] = "X"

    return board

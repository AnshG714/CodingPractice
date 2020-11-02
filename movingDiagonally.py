def movingDiagonal(n, m, x1, y1, x2, y2):
    steps = 0
    visited = set()
    x = x1
    xdir = 1
    y = y1
    ydir = 1
    while True:
        if (x, y) in visited:
            return -1

        if (x, y) == (x2, y2):
            return steps

        visited.add((x, y))

        if (x + xdir >= n or x + xdir < 0) and (y + ydir >= m or y + ydir < 0):
            xdir = -xdir
            ydir = -ydir
            steps += 1
        elif (x + xdir >= n or x + xdir < 0):
            xdir = -xdir
            steps += 1
        elif (y + ydir >= m or y + ydir < 0):
            ydir = -ydir
            steps += 1

        x = x + xdir
        y = y + ydir
        steps += 1

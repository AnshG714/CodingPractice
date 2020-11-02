def alternatingSum(n):
    ns = str(n)
    l = len(ns)
    pos = 0
    neg = 0
    for i in range(0, l, 2):
        pos += int(ns[i])

    for i in range(1, l, 2):
        neg += int(ns[i])

    return pos - neg

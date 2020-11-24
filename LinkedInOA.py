from collections import defaultdict
import math


def numDuplicates(name, price, weight):
    m = defaultdict(int)

    for n, p, w in zip(name, price, weight):
        m[(n, p, w)] += 1

    count = 0
    for k in m:
        count += m[k] - 1

    return count


n = ["ball", "bat", "glove", "glove", "glove"]
p = [2, 3, 1, 2, 1]
w = [2, 5, 1, 1, 1]

#print(numDuplicates(n, p, w))


def maxValue(path, maxStep):
    dp = [-math.inf for _ in range(len(path))]
    dp[0] = path[0]

    for i in range(1, len(dp)):
        for j in range(max(i - maxStep, 0), i):
            dp[i] = max(path[i] + dp[j], dp[i])

    print(dp)
    return max(dp[-maxStep - 1:])


print(maxValue([100, -70, -90, -80, 100], 3))

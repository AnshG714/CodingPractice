def throttlingRequests(requests):
    """
    Look at throttlingGateway.png for specification
    """
    requests.sort()
    f = getRequestFrequencies(requests)
    totalDropped = 0
    last10 = 0
    last60 = 0

    for r in range(len(f)):

        dropped = 0

        if r - 10 >= 0:
            last10 -= f[r - 10]

        if r - 60 >= 0:
            last60 -= f[r - 60]

        last10 += f[r]
        last60 += f[r]

        remainder = f[r]

        if f[r] > 3:
            dropped += f[r] - 3
            remainder -= dropped

        if last10 > 20:
            dropped += last10 - 20
            remainder = max(0, remainder - (last10 - 20))

        if last60 > 30:
            dropped += last60 - 30
            remainder = max(0, remainder - (last60 - 30))

        totalDropped += dropped
        f[r] = remainder

    return totalDropped


def getRequestFrequencies(requests):
    res = [0 for _ in range(requests[-1])]
    for r in requests:
        res[r - 1] += 1

    return res


import collections


def droppedRequests(requestTime):
    requestTime.sort()
    if len(requestTime) <= 3:
        return 0
    count = collections.Counter(requestTime)
    lookup = collections.defaultdict(int)
    for i in range(requestTime[0], requestTime[-1] + 1):
        lookup[i] = lookup[i - 1] + count[i]
    for i in range(3, len(requestTime)):
        temp1, temp2 = 0, 0
        if requestTime[i] - 10 in lookup:
            temp1 = lookup[requestTime[i] - 10]
        if requestTime[i] - 60 in lookup:
            temp2 = lookup[requestTime[i] - 60]
        if requestTime[i - 3] == requestTime[i]:
            requestTime[i - 3] = '$'
        elif i + 1 - temp1 > 20:
            requestTime[i] = '$'
        elif i + 1 - temp2 > 60:
            requestTime[i] = '$'
    return requestTime.count('$')

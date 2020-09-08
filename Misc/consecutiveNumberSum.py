def consecutiveNumberSum(N):
    """
    Given a positive integer N, how many ways can we write it as a sum of consecutive 
    positive integers?

    N = k + (k + 1) + (k + 2) + ... + (k + i)
    N = k * (i + 1) + (i * (i + 1) / 2)
    N - (i * (i + 1) / 2) = k * (i + 1)

    Therefore, N - (i * (i + 1) / 2) should be a multiple of (i + 1)
    """

    counter = 0
    i = 0

    while N - (i * (i + 1) // 2) > 0:
        if (N - (i * (i + 1) // 2)) % (i + 1) == 0:
            counter += 1

        i += 1

    return counter

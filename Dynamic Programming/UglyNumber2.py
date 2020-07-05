def getMaxDivision(a, b):
    """
    Return the number after dividing a with the highest power of b possible
    """

    while a % b != 0:
        a //= b

    return a


def isUgly(n):
    no = getMaxDivision(n, 2)
    no = getMaxDivision(no, 3)
    no = getMaxDivision(no, 5)

    return True if no == 1 else False


def nthUglyNumberBruteForce(n):
    """
    Write a program to find the n-th ugly number.

    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

    Example:

    Input: n = 10
    Output: 12
    Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
    """
    count = 1
    i = 2
    while count < n:
        if isUgly(i):
            count += 1
        i += 1

    return i


def nthUglyNumberDynamic(n):
    i2 = i3 = i5 = 0
    n2 = 2
    n3 = 3
    n5 = 5

    res = [1]

    for _ in range(n - 1):
        nextNum = min(n2, n3, n5)
        res.append(nextNum)

        if n2 == nextNum:
            i2 += 1
            n2 = res[i2] * 2

        if n3 == nextNum:
            i3 += 1
            n3 = res[i3] * 3

        if n5 == nextNum:
            i5 += 1
            n5 = res[i5] * 5

    return res[-1]

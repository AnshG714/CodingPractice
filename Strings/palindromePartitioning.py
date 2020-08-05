def palindromePartitioning(s):
    """
    Given a string s, partition s such that every substring of the partition is a palindrome.

    Return all possible palindrome partitioning of s.

    Example:

    Input: "aab"
    Output:
    [
      ["aa","b"],
      ["a","a","b"]
    ]
    """
    res = []
    partitionUtil(s, 0, [], res)
    return res


def partitionUtil(s, startIndex, curr, res):
    if startIndex >= len(s):
        res.append(curr[:])
        return

    for i in range(startIndex, len(s)):
        if isPalindrome(s, startIndex, i):
            curr.append(s[startIndex:i + 1])
            partitionUtil(s, i + 1, curr, res)
            curr.pop()


def isPalindrome(s, start, end):
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True

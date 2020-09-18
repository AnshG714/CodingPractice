from collections import defaultdict


def maxOccurences(s, maxLetters, minSize, maxSize):
    """
    Given a string s, return the maximum number of ocurrences of any substring 
    under the following rules:

    The number of unique characters in the substring must be less than or equal 
    to maxLetters.
    The substring size must be between minSize and maxSize inclusive.

    Example 1:
    Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
    Output: 2
    Explanation: Substring "aab" has 2 ocurrences in the original string.
    It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

    Example 2:
    Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
    Output: 2
    Explanation: Substring "aaa" occur 2 times in the string. It can overlap.

    Example 3:
    Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
    Output: 3

    Example 4:
    Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
    Output: 0
    """

    start = end = 0
    uniqueCount = 0
    lfreq = defaultdict(int)
    wfreq = defaultdict(int)

    while end - start + 1 <= minSize:
        lfreq[s[end]] += 1
        if lfreq[s[end]] == 1:
            uniqueCount += 1

        end += 1

    if uniqueCount <= maxLetters:
        wfreq[s[start:end]] += 1

    print(wfreq)
    while end < len(s):
        lfreq[s[end]] += 1
        if lfreq[s[end]] == 1:
            uniqueCount += 1

        while end - start + 1 >= maxSize or uniqueCount > maxLetters:
            lfreq[s[start]] -= 1
            if lfreq[s[start]] == 0:
                uniqueCount -= 1

            start += 1

        end += 1
        if minSize <= end - start <= maxSize:
            wfreq[s[start:end]] += 1

    print(wfreq)


def retry(s, maxLetters, minSize, maxSize):
    """
    I was being stupid. maxSize doens't really matter
    """

    letters = set(s[:minSize])
    m = defaultdict(int)
    front = 0
    back = minSize

    while back < len(s):

        if len(letters) <= maxLetters:
            m[s[front:back]] += 1

        front += 1
        back += 1

        letters = set(s[front:back])

    if len(letters) <= maxLetters:
        m[s[front:back]] += 1

    return max(m.values() or [0])

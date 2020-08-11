from collections import defaultdict
import math


def minWindow(s, t):
    """
    Given a string S and a string T, find the minimum window in S which will 
    contain all the characters in T in complexity O(n).

    Example:

    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"
    Note:

    If there is no such window in S that covers all characters in T, return the 
    empty string "".
    If there is such window, you are guaranteed that there will always be only one 
    unique minimum window in S.
    """
    m = defaultdict(int)
    for c in t:
        m[c] += 1

    counter = len(m)
    start = end = 0
    minLen = math.inf
    minStr = ""

    while end < len(s):

        if s[end] in m:
            m[s[end]] -= 1
            if m[s[end]] == 0:
                counter -= 1

        while counter == 0:
            if s[start] in m:
                if m[s[start]] == 0:
                    counter += 1

                m[s[start]] += 1

            if end - start + 1 < minLen:
                minLen = end - start + 1
                minStr = s[start:end + 1]

            start += 1

        end += 1

    return minStr

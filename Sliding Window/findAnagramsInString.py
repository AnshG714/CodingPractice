from collections import defaultdict


def findAnagramsInString(s: str, p: str):
    """
    Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

    Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

    The order of output does not matter.

    Example 1:

    Input:
    s: "cbaebabacd" p: "abc"

    Output:
    [0, 6]

    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    """

    # Initialize
    m = defaultdict(int)
    res = []
    pl = len(p)
    start = end = 0

    # Make base map
    for c in p:
        m[c] += 1

    counter = len(m)

    # template sliding window
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

            if end - start + 1 == pl:
                res.append(start)

            start += 1

        end += 1

    return res

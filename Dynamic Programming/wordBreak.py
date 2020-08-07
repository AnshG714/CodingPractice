def wordBreak(s: str, dic: [str]):
    """
    Given a non-empty string s and a dictionary wordDict containing a list of 
    non-empty words, determine if s can be segmented into a space-separated 
    sequence of one or more dictionary words.

    Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    """
    memo = [False] * (len(s) + 1)
    words = set(dic)
    memo[0] = True

    for i in range(1, len(memo)):
        for j in range(i):
            if s[j:i] in words and memo[j]:
                memo[i] = True

    return memo[-1]

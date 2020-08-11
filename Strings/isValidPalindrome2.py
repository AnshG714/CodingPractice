def valid(s):
    """
    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

    Example 1:

    Input: "aba"
    Output: True
    Example 2:

    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.

    Idea: recurse. When we find a mismatch, we either discard that character, or
    the character on the other side.
    """
    return helper(s, 0, len(s) - 1, True)


def helper(s, start, end, canChange):
    if start >= end:
        return True

    a = start
    b = end

    while a <= b and s[a] == s[b]:
        a += 1
        b -= 1

    if a > b:
        return True
    elif not canChange:
        return False
    else:
        return helper(s, a + 1, b, False) or helper(s, a, b - 1, False)

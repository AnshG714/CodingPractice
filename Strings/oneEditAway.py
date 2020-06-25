def oneEditAway(s: str, t: str) -> bool:
    """
    An edit between two strings is one of the following changes.

    - Add a character
    - Delete a character
    - Change a character

    Given two string s1 and s2, find if s1 can be converted to s2 with exactly one
    edit. Expected time complexity is O(m+n) where m and n are lengths of two strings.
    """
    m, n = len(s), len(t)
    if abs(m - n) >= 2:
        return False

    if n < m:
        s, t = t, s  # m will be the length of the shorter string
        n, m = max(n, m), min(n, m)

    currDiff = 0
    i = 0
    j = 0
    while i < m:
        if s[i] != t[j]:
            if currDiff == 1:
                return False
            elif m < n:
                if s[i] == t[i + 1]:
                    j += 1
                else:
                    return False
            currDiff += 1

        i += 1
        j += 1

    if m < n and j != n and currDiff == 0:
        currDiff += 1

    return currDiff == 1

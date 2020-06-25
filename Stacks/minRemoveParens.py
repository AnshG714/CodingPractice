def minRemoveParens(s):
    banned = set()
    stack = []

    for i in range(len(s)):
        if s[i] == '(':
            banned.add(i)
        elif s[i] == ")":
            if not stack:
                banned.add(i)
            else:
                ind = stack.pop()
                banned.remove(ind)

    res = ""
    for i in range(len(s)):
        if i not in banned:
            res += s[i]

    return res

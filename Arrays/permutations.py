import enchant

# Not only does this permute but this also solves word games for you"


def permutations(s):
    res = []

    def dfs(s, curr):
        if s == "":
            res.append(curr)
            return

        for i in range(len(s)):
            dfs(s[:i] + s[i + 1:], curr + s[i])

    dfs(s, "")
    valid = []
    d = enchant.Dict("en_US")
    for word in res:
        if d.check(word):
            valid.append(word)
    return valid

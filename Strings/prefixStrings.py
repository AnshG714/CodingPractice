def prefixStringsHelper(s, a):
    p = 0
    l = len(s)

    for pre in a:
        if p == len(s):
            return True

        pre_l = len(pre)
        if pre != s[p:p + pre_l]:
            return False

        p += pre_l

    return p == l


def prefixStrings(a, b):
    res = True
    for word in b:
        res = res and prefixStringsHelper(word, a)

    return res

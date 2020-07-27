def convert(s: str):
    count = 0
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    n = len(s)
    i = 0
    while i < n:
        if i < n - 1 and mapping[s[i]] < mapping[s[i + 1]]:
            count += mapping[s[i + 1]] - mapping[s[i]]
            i += 2
        else:
            count += mapping[s[i]]
            i += 1

    return count

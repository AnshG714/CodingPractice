def letterCombos(digits):
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    output = []

    def dfs(currString, digits):
        if digits == "":
            output.append(currString)
            return

        for c in mapping[digits[0]]:
            dfs(currString + c, digits[1:])

    dfs("", digits)
    return output

def generateParentheses(n):
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:

    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]
    """
    output = []

    def dfs(l, r, n, currString):
        # If the opening and closing parentheses together have a length of 2 * l,
        # we know we have the required string.
        if l + r == 2 * n:
            output.append(currString)

        # do a depth first search if the number of opening parens is less than max
        if l < n:
            dfs(l + 1, r, n, currString + '(')

        # if the number of closing parens is less than the opening parens, complete that.
        if r < l:
            dfs(l, r + 1, n, currString + ')')

    dfs(0, 0, n, "")
    return output

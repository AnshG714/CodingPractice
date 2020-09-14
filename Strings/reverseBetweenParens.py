def reverse(s):
    if s == "":
        return s
    return reverse(s[1:]) + s[0]


def reverseBetweenParens(s):
    """
    Write a function that reverses characters in (possibly nested) parentheses in 
    the input string.

    Input strings will always be well-formed with matching ()s.

    For inputString = "(bar)", the output should be
    reverseInParentheses(inputString) = "rab";

    For inputString = "foo(bar)baz(blim)", the output should be
    reverseInParentheses(inputString) = "foorabbazmilb"

    For inputString = "foo(bar(baz))blim", the output should be
    reverseInParentheses(inputString) = "foobazrabblim".
    Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
    """

    stack = []

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ")":
            opening = stack.pop()
            temp = reverse(s[opening + 1:i])
            s = s[:opening + 1] + temp + s[i:]

    res = ""
    for c in s:
        if c not in "()":
            res += c

    return res

import operator


def tokenize(s: str) -> [str]:
    """Tokenizes an input expression given as a string to a string array, where
    every element of an array is either a stringified integer or an operator 
    (one of '+', '-' and '*').

    Assumes there are no whitespaces in s. 

    Example 1:
        "2+4*3-5" -> ['2', '+', '4', '*', '3', '-', '5']
        "12-45+0" -> ['12', '-', '45', '+', '0']

    Args:
        s (str): The input expression string

    Returns:
        [str]: The tokenized output
    """

    s += "+"
    currNum = 0
    res = []
    for c in s:
        if c.isdigit():
            currNum = 10 * currNum + int(c)
        else:
            res.append(str(currNum))
            currNum = 0
            res.append(c)

    return res[:-1]


def processBaseOp(sint1: str, op: str, sint2: str) -> int:
    """Computes a basic calculation using an operator string and 2 stringified
    integers

    Args:
        sint1 (str): The first stringified integer
        op (str): The operator, one of '+', '-', '*'
        sint2 (str): The second stringified integer

    Returns:
        int: A computation based on <sint1> <op> <sint2>
    """
    mapping = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    return mapping[op](int(sint1), int(sint2))


def diffWaysToAddParens(arr: [int], res: set):
    n = len(arr)
    if n == 1:
        res.add(arr[0])
        return

    elif n == 3:
        res.add(processBaseOp(*arr))
        return

    else:
        for i in range(0, n - 2, 2):
            mid = arr[i:i + 3]
            before = arr[:i]
            later = arr[i + 3:]
            newArr = before + [str(processBaseOp(*mid))] + later
            diffWaysToAddParens(newArr, res)


def solve(s: str):
    res = set()
    arr = tokenize(s)
    diffWaysToAddParens(arr, res)
    return list(res)

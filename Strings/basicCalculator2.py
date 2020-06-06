def basicCalc(s):
    """
    Implement a basic calculator to evaluate a simple expression string.

    The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

    Example 1:

    Input: "3+2*2"
    Output: 7
    Example 2:

    Input: " 3/2 "
    Output: 1
    Example 3:

    Input: " 3+5 / 2 "
    Output: 5
    """
    s += "+"
    i = 0
    numAcc = 0
    addList = []
    while i < len(s):
        print("i", i)
        if s[i].isdigit():
            numAcc = 10*numAcc + int(s[i])

        elif s[i] == "+":
            addList.append(numAcc)
            numAcc = 0

        elif s[i] == "-":
            addList.append(-numAcc)
            numAcc = 0

        elif s[i] == "*" or s[i] == "/":
            curr = i
            temp = numAcc
            numAcc = 0
            print("temp", temp)
            while i < len(s) and (not s[i].isdigit() or s[i] == " "):
                i += 1
                if s[i].isdigit():
                    numAcc = 10*numAcc + int(s[i])
            print("final", numAcc)
            if s[curr] == "*":
                print("appending", temp * numAcc)
                addList.append(temp * numAcc)
            else:
                addList.append(temp // numAcc)

            numAcc = 0

        i += 1
        print(addList)

    return sum(addList)

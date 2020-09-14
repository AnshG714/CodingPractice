def textJustification(words, maxWidth):
    """
    Given an array of words and a width maxWidth, format the text such that each
    line has exactly maxWidth characters and is fully (left and right) justified.

    You should pack your words in a greedy approach; that is, pack as many words
    as you can in each line. Pad extra spaces ' ' when necessary so that each
    line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. If
    the number of spaces on a line do not divide evenly between words, the empty
    slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left justified and no extra space is
    inserted between words.

    Note:

    * A word is defined as a character sequence consisting of non-space characters only.
    * Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    * The input array words contains at least one word.

    Example 1:

    Input:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    Output:
    [
      "This    is    an",
      "example  of text",
      "justification.  "
    ]

    Example 2:

    Input:
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    Output:
    [
      "What   must   be",
      "acknowledgment  ",
      "shall be        "
    ]
    Explanation: Note that the last line is "shall be " instead of "shall be",
      because the last line must be left-justified instead of fully-justified.
    Note that the second line is also left-justified becase it contains only one word.

    Example 3:

    Input:
    words = ["Science","is","what","we","understand","well","enough","to","explain",
      "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    Output:
    [
      "Science  is  what we",
      "understand      well",
      "enough to explain to",
      "a  computer.  Art is",
      "everything  else  we",
      "do                  "
    ]
    """
    lines = []
    currWordLen = 0
    temp = []

    # split up into different lines.

    # ensure everything before gets appended properly
    words.append('a' * maxWidth)

    for word in words:
        if len(word) + currWordLen > maxWidth:
            lines.append(temp)
            temp = []
            temp.append(word)
            currWordLen = len(word) + 1  # account for spaces
        else:
            temp.append(word)
            currWordLen += len(word) + 1

    res = []
    numLines = len(lines)
    for index, line in enumerate(lines):
        if index == numLines - 1:
            numWords = len(line)
            s = ' '.join(line)
            remainingSpaces = maxWidth - len(s)
            s += ' ' * remainingSpaces
            res.append(s)
        else:

            numWords = len(line)
            remainingSpaces = maxWidth - len(''.join(line))
            if numWords - 1 != 0:
                interSpace = remainingSpaces // (numWords - 1)
                remainingSpaces = remainingSpaces - \
                    ((numWords - 1) * interSpace)

            i = 0
            while remainingSpaces != 0:
                line[i] += ' '
                i = (i + 1) % (numWords)
                remainingSpaces -= 1

            res.append((' ' * interSpace).join(line))

    return res

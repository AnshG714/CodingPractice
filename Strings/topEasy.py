from collections import defaultdict


def reverseString(chars):
    """
    Write a function that reverses a string. The input string is given as an array
    of characters char[].

    Do not allocate extra space for another array, you must do this by modifying
    the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.
    """
    p1 = 0
    p2 = len(chars) - 1

    while p1 < p2:
        chars[p1], chars[p2] = chars[p2], chars[p1]
        p1 += 1
        p2 -= 1

    return chars


def romanToInt(s):
    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, two is written as II in Roman numeral, just two one's added
    together. Twelve is written as, XII, which is simply X + II. The number
    twenty seven is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right.
    However, the numeral for four is not IIII. Instead, the number four is written
    as IV. Because the one is before the five we subtract it making four. The same
    principle applies to the number nine, which is written as IX. There are six
    instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

    Given a roman numeral, convert it to an integer. Input is guaranteed to be
    within the range from 1 to 3999.
    """

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
        if i == n - 1:
            count += mapping[s[i]]
            i += 1
        else:
            if mapping[s[i]] < mapping[s[i + 1]]:
                count += mapping[s[i + 1]] - mapping[s[i]]
                i += 2
            else:
                count += mapping[s[i]]
                i += 1

    return count


def firstUnique(s):
    """
    Given a string, find the first non-repeating character in it and return it's
    index. If it doesn't exist, return -1.
    """

    dic = defaultdict(int)

    for char in s:
        dic[char] += 1

    for i in range(len(s)):
        if dic[s[i]] == 1:
            return i

    return -1


def countAndSay(n):
    """
    The count-and-say sequence is the sequence of integers with the first five
    terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say
    sequence. You can do so recursively, in other words from the previous member
    read off the digits, counting the number of digits in groups of the same digit.

    Note: Each term of the sequence of integers will be represented as a string.
    """

    if n == 1:
        return "1"

    prevMember = countAndSay(n - 1)

    # 2nd entry: "11"
    print(n - 1, ": ", prevMember)
    curr = prevMember[0]  # "" prevMember[0]  # curr = "1"
    res = ""
    i = 1
    currCount = 1

    while i < len(prevMember):
        if curr == prevMember[i]:
            currCount += 1
        else:
            res += str(currCount) + prevMember[i - 1]
            curr = prevMember[i]
            currCount = 1

        i += 1

    res += str(currCount) + prevMember[-1]
    return res


def validPalindrome(s):
    """
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.

    Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true
    Example 2:

    Input: "race a car"
    Output: false
    """

    p1 = 0
    p2 = len(s) - 1

    while p1 <= p2:
        if s[p1].isalnum() and s[p2].isalnum():
            if s[p1].lower() == s[p2].lower():
                p1 += 1
                p2 -= 1
            else:
                return False
        elif not s[p1].isalnum():
            p1 += 1
        else:
            p2 -= 1

    return True


def longestCommonPrefix(lst):
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
    """
    res = ""
    curr = ""
    pointer = 0

    while lst:
        for index, word in enumerate(lst):

            if pointer >= len(word):
                return res

            if index == 0:
                curr = word[pointer]

            elif word[pointer] != curr:
                return res

        res += curr
        pointer += 1

    return res


def strStr(haystack, needle):
    """
    Implement strStr().

    Return the index of the first occurrence of needle in haystack, or -1 if 
    needle is not part of haystack.

    Example 1:

    Input: haystack = "hello", needle = "ll"
    Output: 2
    Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1
    """

    # mississipi
    #     issip

    h_pointer = 0
    n = len(needle)
    while h_pointer + n <= len(haystack):
        if haystack[h_pointer:h_pointer + n] == needle:
            return h_pointer

        h_pointer += 1

    return -1


def canFormPalindrome(s):
    """
    Given a string, determine if a permutation of the string could form a palindrome.

    For example,
    "code" -> False, "aab" -> True, "carerac" -> True.
    """

    countMap = defaultdict(int)
    for c in s:
        countMap[c] += 1

    oddFound = False
    for c in s:
        if countMap[c] % 2 == 1:
            if oddFound:
                return False
            oddFound = True

    return True


def excelSheetNumber(s):
    """
    Given a column title as appear in an Excel sheet, return its corresponding column number.

    For example:

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28 
    """

    def findLetterPos(char):
        return ord(char) - ord('A') + 1

    tile = 0
    n = len(s)
    for i in range(n):
        # This is needed to 'shift' by the total number of letters.
        title = tile * 26
        # Analogy: Similar to how powers of 10 work.
        tile += findLetterPos(s[i])

    return tile


def excelSheetColumn(num):
    """ opposite of above"""

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while num:
        last = num % 26
        res = alpha[last - 1] + res
        num //= 26
        if last == 0:
            num -= 1

    return res

from collections import defaultdict

"""
Given an array of size n, find the majority element. The majority element is the 
element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist
in the array.
"""


def majorityElement(nums):
    dic = defaultdict(int)

    for num in nums:
        dic[num] += 1

    n = len(nums)
    for num in nums:
        if dic[num] > n//2:
            return num


"""
                                  GOOD

Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Example Cases:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
0     i       j       n
- - - - - - - - - - - 

invariant:
- everything between [0, i) to be a number != 0, in the order it presents itself
in the original array
- Everything between [i, j) is 0

Everything after j is unknown. 
Implied: j >= i

"""


def moveZeroes(nums):
    # initialize two pointers, i and j, to 0
    i = j = 0

    # j is the 'fast' pointer
    while j < len(nums):
        # case 1: nums[j] == 0
        if nums[j] == 0:
            j += 1
        else:
            # case 2: nums[j] != 0
            # swap numbers at indices i and j
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

    return nums


"""
Say you have an array prices for which the ith element is the price of a given 
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many 
transactions as you like (i.e., buy one and sell one share of the stock multiple 
times).

Note: You may not engage in multiple transactions at the same time (i.e., you 
must sell the stock before you buy again).
"""


def bestTimeToBuyAndSellStock2(nums):
    profit = 0
    for i in range(len(nums) - 1):
        if nums[i] < nums[i+1]:
            profit += nums[i+1] - nums[i]

    return profit


"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the 
array, and it should return false if every element is distinct.
"""


def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


def generatePascals(numRows):
    """
    Given a non-negative integer numRows, generate the first `numRows` of Pascal's 
    triangle.
    """
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        res = [[1], [1, 1]]
        for i in range(3, numRows+1):
            temp = [1]

            for j in range(i-2):
                newEl = res[-1][j] + res[-1][j+1]
                temp.append(newEl)

            temp.append(1)

            res.append(temp)

        return res

from collections import defaultdict
import math


def majorityElement(nums):
    """
    Given an array of size n, find the majority element. The majority element is the 
    element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority element always exist
    in the array.
    """

    dic = defaultdict(int)

    for num in nums:
        dic[num] += 1

    n = len(nums)
    for num in nums:
        if dic[num] > n//2:
            return num


def moveZeroes(nums):
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


def bestTimeToBuyAndSellStock2(nums):
    """
    Say you have an array prices for which the ith element is the price of a given 
    stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many 
    transactions as you like (i.e., buy one and sell one share of the stock multiple 
    times).

    Note: You may not engage in multiple transactions at the same time (i.e., you 
    must sell the stock before you buy again).
    """
    profit = 0
    for i in range(len(nums) - 1):
        if nums[i] < nums[i+1]:
            profit += nums[i+1] - nums[i]

    return profit


def containsDuplicate(nums):
    """
    Given an array of integers, find if the array contains any duplicates.

    Your function should return true if any value appears at least twice in the 
    array, and it should return false if every element is distinct.
    """
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


def generatePascals(numRows):
    """
                                    GOOD

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


def missingNumber(nums):
    """
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find 
    the one that is missing from the array.
    """

    # idea: if all the numbers were included, the sum of the array would be n(n+1)/2
    n = len(nums)
    return n*(n+1)//2 - sum(nums)


def maxSubarray(nums):
    """
    Given an integer array nums, find the contiguous subarray (containing at least 
    one number) which has the largest sum and return its sum.
    """
    maxSum = -math.inf
    currSum = 0
    for num in nums:
        currSum += num
        maxSum = max(currSum, maxSum)

        if currSum < 0:
            currSum = 0

    return maxSum


def bestTimeToBuyAndSellStock(nums):
    """
                                  GOOD: Review again. 

    Say you have an array for which the ith element is the price of a given stock 
    on day i.

    If you were only permitted to complete at most one transaction (i.e., buy one 
    and sell one share of the stock), design an algorithm to find the maximum 
    profit.

    Note that you cannot sell a stock before you buy one.

    [1, 2, 3, 0, 7, 6, 2]
    """

    # idea: We want to maximize the difference between the 2 prices p[i], p[j],
    # where j >= i

    # we can do a one pass algorithm. Keep track of the minimum number. If we
    # find a new minimum, store that minimum. Otherwise, compute new max profit

    minPrice = math.inf
    maxProfit = 0

    for num in nums:
        if num < minPrice:
            minPrice = num
        else:
            maxProfit = max(maxProfit, num - minPrice)

    return maxProfit


def twoSum(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they 
    add up to a specific target.

    You may assume that each input would have exactly one solution, and you may 
    not use the same element twice.
    """

    mapping = defaultdict(int)
    for index, value in enumerate(nums):
        mapping[value] = index

    for num in nums:
        otherNum = target - num
        if otherNum in mapping and mapping[otherNum] != mapping[num]:
            return [mapping[num], mapping[otherNum]]

    return [-1, -1]


def removeDupsFromSorted(nums):
    """
                              GOOD: REVIEW

    Given a sorted array nums, remove the duplicates in-place such that each 
    element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by modifying 
    the input array in-place with O(1) extra memory.

    [1,1,2] -> [1, 2, rando element]

    invariant:
    - [, slow] is unique
    - (slow, fast] are all duplicates
    - (fast, ...] are unknown. 
    """

    if nums == []:
        return 0

    slow = fast = 0
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]

    return nums, (slow + 1)


def addOne(nums):
    """
    Given a non-empty array of digits representing a non-negative integer, plus 
    one to the integer.

    The digits are stored such that the most significant digit is at the head of 
    the list, and each element in the array contain a single digit.

    You may assume the integer does not contain any leading zero, except the 
    number 0 itself.
    """

    pointer = len(nums) - 1
    carry = 1

    while pointer >= 0:
        newVal = nums[pointer] + carry
        carry = newVal // 10
        nums[pointer] = newVal % 10
        pointer -= 1

    if carry != 0:
        nums.insert(0, 1)

    return nums

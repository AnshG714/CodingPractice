from Stack import *


def dailyTemperature(temps):
    """
                                GOOD TO REVIEW

    Given a list of daily temperatures T, return a list such that, for each day in 
    the input, tells you how many days you would have to wait until a warmer 
    temperature. If there is no future day for which this is possible, put 0 instead.

    For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
    your output should be [1, 1, 4, 2, 1, 1, 0, 0].

    Note: The length of temperatures will be in the range [1, 30000]. Each 
    temperature will be an integer in the range [30, 100].


    Idea: 
     - Traverse list from back
     - Maintain the following invariant: Every NEW element on the stack will be 
       less than or equal to all the later elements (s[-1] < s[-2] < s[-3]), 
       where s[-1] represents the top of the stack
     - If there are elements in the stack, then compare the current element to
       the topmost element. Keep popping until the current element in the temps
       array is less than or equal to the top of the array
     - When we stop popping, there are two conditions - either there are no more
       elements left to pop, or the top element of the stack is greater than the 
       current element in the temps array. This will also be the next possible 
       warmer day, and the number of days between them is the index of the element
       at the top of the stack, and the current element in the array.
     - If there is no element in the stack, then there can be no potential warmer
       day

    """
    s = Stack()
    p = len(temps) - 1
    res = [0] * len(temps)
    while p >= 0:
        currTemp = temps[p]

        while not s.isEmpty() and s.peek()[0] < currTemp:
            s.pop()

        if not s.isEmpty():
            res[p] = s.peek()[1] - p

        s.push((temps[p], p))
        p -= 1

    return res


def dailyTemperatureReversed(temps):
    """
    Same as above, except with forward traversal of the list
    """

    s = Stack()
    res = [0] * len(temps)
    p = 0
    while p < len(temps):
        currTemp = temps[p]
        while not s.isEmpty() and s.peek()[0] <= currTemp:
            _, index = s.pop()
            res[index] = p - index

        s.push((temps[p], p))
        p += 1

    return res


def nextGreaterNumber(nums1, nums2):
    """
    You are given two arrays (without duplicates) nums1 and nums2 where nums1’s 
    elements are subset of nums2. Find all the next greater numbers for nums1's 
    elements in the corresponding places of nums2.

    The Next Greater Number of a number x in nums1 is the first greater number to 
    its right in nums2. If it does not exist, output -1 for this number.

    Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
    Output: [-1,3,-1]

    Input: nums1 = [2,4], nums2 = [1,2,3,4].
    Output: [3,-1]
    """
    nxt = {}
    stack = []

    p = len(nums2) - 1
    while p >= 0:

        while stack and stack[-1] <= nums2[p]:
            stack.pop()

        if stack:
            nxt[nums2[p]] = stack[-1]
        else:
            nxt[nums2[p]] = -1

        stack.append(nums2[p])
        p -= 1

    res = []
    for num in nums1:
        res.append(nxt[num])

    return res

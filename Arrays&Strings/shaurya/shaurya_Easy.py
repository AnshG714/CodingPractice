from collections import defaultdict

"""
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

def majorityElement(nums):
    dic = defaultdict(int) # NEW: defaultdict(datatype) will work after: "from collections import defaultdict" at the top

    n = len(nums)

    for num in nums:

        dic[num] += 1

        if dic[num] > n//2: # IMP: / is normal float division while // is integer or floow division. So, 5/2 = 2.5 and 5//2 = 2
            return num


"""
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

"""
Main Idea:

To do this in place:
    - have two pointers i and j
    - have invariants

Here, i is the slow pointer and j is the fast pointer. Also, j >= i

Invariants:
    - Everything in nums[0, i) must not be zero
    - Everthing in nums[i,j) must be zero
    - Everything after j does not matter.

"""

def moveZeroes(nums):

    i=j=0

    n = len(nums)

    while j != n:
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
        
        j+=1
     
    return nums

"""
122. Best Time to Buy and Sell Stock II

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4
"""
def maxProfit(nums):

    profit = 0

    for i in range(len(nums)-1):
        if nums[i+1] > nums[i]:
            profit += nums[i+1] - nums[i]

    return profit

"""
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def containsDuplicates(nums):
    l = []

    for num in nums:
        if num in l:
            return True
        l.append(num)
    return False




"""
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
def pascalsTriangle(numRows):
    newRow=[0] * numRows
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1,1]]
    else:
        res = [[1],[1,1]]

        for i in range(3, numRows+1):
            oldRow = res[-1]
            print(oldRow)
            print("Hello")
            print(oldRow)
            newRow = []
            newRow.append(1)
            print(newRow)
            for j in range(1, numRows-1):
                newRow.append(oldRow[j-1]+oldRow[j])
            newRow.append(1)
            res.append(newRow)
        # print(newRow)
        
    
    return res



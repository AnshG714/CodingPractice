import math


def findMajority(nums):
    """
    Find all the elements in nums that occur more than n // 3 times. 

    Idea: Moore's voting algorithm. 
    - FInd 2 candidates for the majority (there can be at most 2)
    - Maintain count for 2 majority elements
    - If the next element is same then increment the counts if the next element is 
    not same then decrement the counts.
    - if the count reaches 0 then changes the maj_index to the current element and 
    set the count again to 1.
    - Now again traverse through the array and find the count of majority element found.
    - If the count is greater than half the size of the array, it's a majority element
    """
    # Initializing counts
    c1 = c2 = 0
    first = second = math.inf

    # First pass
    for num in nums:
        if num == first:
            c1 += 1
        elif num == second:
            c2 += 1
        elif c1 == 0:
            c1 += 1
            first = num
        elif c2 == 0:
            c2 += 1
            second = num
        else:
            c1 -= 1
            c2 -= 1

    # Second pass
    c1 = c2 = 0
    for num in nums:
        if num == first:
            c1 += 1
        elif num == second:
            c2 += 1

    n = len(nums)
    res = []
    if c1 > n // 3:
        res.append(first)

    if c2 > n // 3:
        res.append(second)

    return res

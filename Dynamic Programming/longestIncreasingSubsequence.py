def longestIncreasingSubsequence(nums):
    """
    Given an unsorted array of integers, find the length of longest increasing subsequence.

    Example:

    Input: [10,9,2,5,3,7,101,18]
    Output: 4 
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

    IDEA: Straight-forward DP. 

    Fix an element. For every element that's greater than  this fixed element and comes before it,
    compute max(memo[element], memo[prev element] + 1)

    Time complexity: O(n2)
    """
    if not nums:
        return 0

    memo = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                memo[i] = max(memo[j] + 1, memo[i])

    return max(memo)

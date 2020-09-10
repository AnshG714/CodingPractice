from collections import defaultdict
import math


def degreeOfArray(nums):
    """
    Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

    Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

    Example 1:

    Input: [1, 2, 2, 3, 1]
    Output: 2
    Explanation:
    The input array has a degree of 2 because both elements 1 and 2 appear twice.
    Of the subarrays that have the same degree:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    The shortest length is 2. So return 2.

    Example 2:

    Input: [1,2,2,3,1,4,2]
    Output: 6
    """

    # Generate frequency map
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1

    degree = max(freq.values())
    freq2 = defaultdict(int)
    minLen = math.inf

    start = end = 0
    maxCount = 0

    # sliding window
    while end < len(nums):
        freq2[nums[end]] += 1
        if freq2[nums[end]] == degree:
            maxCount += 1

        while maxCount > 0:
            if freq2[nums[start]] == degree:
                maxCount -= 1

            freq2[nums[start]] -= 1
            minLen = min(minLen, end - start + 1)
            start += 1

        end += 1

    return minLen

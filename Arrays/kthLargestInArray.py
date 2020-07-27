import random


def kthSmallestInArray(nums, k):
    left = 0
    right = len(nums) - 1
    while left <= right:
        p = partition(nums, left, right)
        if p == k - 1:
            return nums[p]
        elif p > k - 1:
            right = p - 1
        else:
            left = p + 1
            # k - p (that's the offset required) - 1 (because of 0 indexing) + left (because we also want to search for an index after our left shift)
            k = k - p + left - 1

    return -1


def partition(nums, left, right):
    pivot = random.randint(left, right)
    nums[pivot], nums[right] = nums[right], nums[pivot]
    pval = nums[right]

    i = j = right - 1

    while i >= left:
        if nums[i] < pval:
            i -= 1
        else:
            nums[i], nums[j + 1] = nums[j + 1], nums[i]
            nums[i], nums[j] = nums[j], nums[i]
            i -= 1
            j -= 1

    return j + 1

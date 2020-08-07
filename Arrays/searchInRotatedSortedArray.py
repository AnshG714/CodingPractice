def search(nums, target):
    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to 
    you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    You are given a target value to search. If found in the array return its index, 
    otherwise return -1.

    You may assume no duplicate exists in the array.
    """

    pivot = findPivot(nums)
    if pivot == -1:
        return binarySearch(nums, 0, len(nums) - 1, target)
    elif nums[0] <= target <= nums[pivot]:
        return binarySearch(nums, 0, pivot, target)
    else:
        return binarySearch(nums, pivot + 1, len(nums) - 1, target)


def binarySearch(nums, left, right, target):

    if left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binarySearch(nums, left, mid - 1, target)
        else:
            return binarySearch(nums, mid + 1, right, target)

    return -1


def findPivot(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
            return mid
        elif nums[left] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

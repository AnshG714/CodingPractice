def maximumSumSubarray(nums):

    curr_max = global_max = nums[0]
    for i in range(1, len(nums)):
        curr_max = max(nums[i], nums[i] + curr_max)
        if curr_max > global_max:
            global_max = curr_max

    return global_max


def maxProductSubarray(nums):

    curr_max = curr_min = global_max = nums[0]
    for i in range(1, len(nums)):
        curr_max, curr_min = max(nums[i] * curr_max, nums[i] * curr_min, nums[i]), min(
            nums[i] * curr_max, nums[i] * curr_min, nums[i])
        global_max = max(global_max, curr_max)

    return global_max

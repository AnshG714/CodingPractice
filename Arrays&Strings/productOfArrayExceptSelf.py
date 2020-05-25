def productOfArrayExceptSelf(nums):
    """
    Given an array nums of n integers where n > 1,  return an array output such 
    that output[i] is equal to the product of all the elements of nums except nums[i].

    Example:

    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    Constraint: It's guaranteed that the product of the elements of any prefix or 
    suffix of the array (including the whole array) fits in a 32 bit integer.

    Note: Please solve it without division and in O(n).
    """

    # idea: make prefix and suffix arrays. pref[i] will store the product
    # of all the numbers to the LEFT of arr[i], suff[i] will store all the product
    # of the numbers to the RIGHT of arr[i]
    n = len(nums)
    pref = [1] * n
    suff = [1] * n
    res = [1] * n

    # fill in prefix array
    for i in range(1, len(nums)):
        pref[i] = pref[i-1] * nums[i-1]

    # fill in suffix array
    for i in range(len(nums)-2, -1, -1):
        suff[i] = suff[i+1] * nums[i+1]

    for i in range(len(nums)):
        res[i] = pref[i] * suff[i]

    return res

############################### VERY IMPORTANT ##############################


def findDuplicate(nums):
    """
    Given an array nums containing n + 1 integers where each integer is between 
    1 and n (inclusive), prove that at least one duplicate number must exist. 
    Assume that there is only one duplicate number, find the duplicate one.

    Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated 
    more than once.


    Idea: consider the problem as a linked list problem. Every entry is a node,
    and the next node is nums[that number]. If there's a duplicate, they'll both
    point to the same element! Hence, a cycle in a linked list forms. 

    """
    hare = tortoise = nums[0]
    while True:
        hare = nums[nums[hare]]
        tortoise = nums[tortoise]
        if hare == tortoise:
            break

    hare = nums[0]

    while hare != tortoise:
        hare = nums[hare]
        tortoise = nums[tortoise]

    return hare

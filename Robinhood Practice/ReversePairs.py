from collections import defaultdict


def reversePairs(nums):
    """
    Problem specification in ReversePairs.png.
    Note that num1 + rev(num2) = num2 + rev(num1) === num1 - rev(num1) = num2 - rev(num2)

    Idea is simple, just use a HashMap to store all the indices whhere the sum 
    = num_i + rev(num_i). Then, we can simply calculate the total number of pairs
    in each 'bucket'.
    """
    m = defaultdict(list)
    for i in range(len(nums)):
        rev_num = int(str(nums[i])[::-1])
        print(rev_num)
        m[nums[i] - rev_num].append(i)

    count = 0
    print(m)
    for val in m:
        n = len(m[val])
        count += (n * (n + 1)) // 2

    return count

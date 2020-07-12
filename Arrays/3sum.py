from collections import defaultdict


def threeSum(nums):

    seen = set()
    hashMap = defaultdict(int)

    for num in nums:
        hashMap[num] += 1

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            target = -(nums[i] + nums[j])
            hashMap[nums[i]] -= 1
            hashMap[nums[j]] -= 1
            if target in hashMap and hashMap[nums[i]] >= 0 and hashMap[nums[j]] >= 0 and hashMap[target] > 0:
                newList = sorted([nums[i], nums[j], target])
                tup = tuple(newList)
                seen.add(tup)

            hashMap[nums[i]] += 1
            hashMap[nums[j]] += 1

    return [list(tup) for tup in seen]

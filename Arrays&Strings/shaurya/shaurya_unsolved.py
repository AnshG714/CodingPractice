def subsets(nums):
    res = []
    for i in range(len(nums)):
        oldEl = [nums[i]]
        res.append(oldEl)


        for j in range(i+1, len(nums)):
            for a in range(num.length-i):
                
            newEl =oldEl[:] # IMP: this is a deep copy
            newEl.append(nums[j])
            res.append(newEl)

    return res
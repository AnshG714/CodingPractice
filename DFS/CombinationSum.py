def combinationSum(candidates, target):
    """
    Given a set of candidate numbers (candidates) (without duplicates) and a 
    target number (target), find all unique combinations in candidates where the 
    candidate numbers sums to target.

    The same repeated number may be chosen from candidates unlimited number of 
    times.

    Note:

    * All numbers (including target) will be positive integers.
    * The solution set must not contain duplicate combinations.

    Example 1:

    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
    [7],
    [2,2,3]
    ]
    """

    candidates.sort()
    res = []

    def dfs(curr, currSum):
        if currSum > target:
            return
        elif currSum == target:
            res.append(curr[:])
            return
        else:
            for cand in candidates:
                if not curr or curr[-1] <= cand:
                    curr.append(cand)
                    dfs(curr, currSum + cand)
                    curr.pop()

    dfs([], 0)
    return res

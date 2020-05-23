def subsets(nums):
  """
  Given a set of distinct integers, nums, return all possible subsets (the power set).

  Note: The solution set must not contain duplicate subsets
  """

  # recursive approach - if we have a power set of all numbers of nums except the 
  # last one, then how do we add a new element? Basically, copy the previous 
  # result, and add this element to each of the copied arrays. 

  """
  [1,2,3,4]

  [[]]
  [[], [1]]

  [[], [1], [2], [1,2]]

  [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

  [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3], [4], [1, 4], [2, 4], [1,2, 4], 
  [3, 4], [1,3, 4], [2,3, 4], [1,2,3, 4]]

  """

  if nums == []:
    return [[]]

  temp = subsets(nums[:-1])
  n = len(temp)
  for i in range(n):
    new = temp[i][:]
    new.append(nums[-1])
    temp.append(new)

  return temp



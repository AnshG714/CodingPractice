def buyAndSellStockWithCooldown(nums):
  """
  Say you have an array for which the ith element is the price of a given stock on day i.

  Design an algorithm to find the maximum profit. You may complete as many 
  transactions as you like (ie, buy one and sell one share of the stock multiple 
  times) with the following restrictions:

  You may not engage in multiple transactions at the same time (ie, you must 
  sell the stock before you buy again).
  After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
  """

  # idea: Dynamic programming. Keep track of two arrays (buy and sell), and 
  # keep track of the max profit on day i if you choose to either buy on day i
  # or sell on day i. Firstly, on day 1, max profit when the action is to buy
  # is -nums[0], and max profit on selling on the first day is 0 (technically
  # have nothing to sell). 

  # Next, the max profit if we buy on day i is either 
  # (i) we choose to not buy => profit is the same as buy[i - 1]
  # (ii) or we choose to buy, => the profit will be sell[i - 2] - nums[i]
  # (to account for cooldown)

  # On the other hand, if we choose to sell it, we have two options again:
  # (i) We choose to not sell => profit is the same as sell[i - 1]
  # (ii) We choose to sell => Profit is buy[i - 1] + nums[i] (since we want the
  # last profit that we bought our stock with, and since we're selling our stock
  # we can add that)

  n = len(nums)
  if n <= 1:
    return 0

  # Initialize memoization arrays
  sell = [0] * n
  buy = [0] * n

  buy[0] = -nums[0]

  for i in range(1, n):
    buy[i] = max(buy[i-1], (sell[i - 2] if i - 2 >= 0 else 0) - nums[i])
    sell[i] = max(sell[i - 1], buy[i - 1] + nums[i])

  return sell[-1]
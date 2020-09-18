def stockBot(prices, bot, k):
    """
    Idea: Simple sliding window. Initialize revenue if the first k entries were 
    made 1, and then move the window.

    If the element that leaves the window on the left was originally a 0, then
    subtract 2 * price[element]

    If the element that enters the window was originally buy, add 2 * price[element]
    """

    # Initialize revenue
    revenue = 0
    for i in range(len(prices)):
        if i < k:
            revenue += prices[i]
        else:
            if bot[i] == 1:
                revenue += prices[i]
            else:
                revenue -= prices[i]

    start = 0
    maxRevenue = revenue
    # start moving sliding window

    for i in range(len(prices) - k):

        if bot[start] == 0:
            revenue -= 2 * prices[start]

        if bot[i + k] == 0:
            revenue += 2 * prices[i + k]

        start += 1

        maxRevenue = max(maxRevenue, revenue)

    return maxRevenue

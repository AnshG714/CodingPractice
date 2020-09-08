import heapq


class Bid:
    def __init__(self, ide, shares, price, timestamp):
        self.id = ide
        self.shares = shares
        self.price = price
        self.timestamp = timestamp

    def __lt__(self, value):
        if self.price == value.price:
            return self.timestamp < value.timestamp

        return self.price > value.price


def ipo(bids, totalShares):
    h = []
    for bid in bids:
        heapq.heappush(h, Bid(*bid))

    while totalShares > 0 and h:
        top: Bid = heapq.heappop(h)
        totalShares -= top.shares

    return [user.id for user in h]

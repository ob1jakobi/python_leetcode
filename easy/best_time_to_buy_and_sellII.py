

def maxProfit(prices: list[int]) -> int:
    """
    You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`th day.
    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock
    at any time. However, you can buy it then immediately sell it on the same day.
    Find and return the maximum profit you can achieve.

    Examples:
    >>> maxProfit([7,1,5,3,6,4])
    7
    >>> maxProfit([1,2,3,4,5])
    4
    >>> maxProfit([7,6,4,3,1])
    0
    """
    total_profit = 0
    i = 0            # pointer for the currently-owned stock value
    j = 1            # pointer for the newest stock price/value
    while j < len(prices):
        current_price = prices[i]
        new_price = prices[j]
        # Buy when the new_price < current_price (buy low)
        if new_price < current_price:
            i = j
        # Sell when the new_price > current_price (sell high)
        elif new_price > current_price:
            # calcuate profit
            profit = new_price - current_price
            total_profit += profit
            # set the i pointer to the new price (j) pointer
            i = j
        # increment j to point to the next day's prices
        j += 1
    return total_profit


if __name__ == "__main__":
    import doctest
    doctest.testmod(name="maxProfit", verbose=True)

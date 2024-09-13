class Solution(object):
    def maxProfit(self, prices):
        # Initialize Max Profit to 0, in the case that there is no max profit.
        max_profit = 0
        left = 0 # representing the index we buy stock.
        right = 1 # representing the index we sell stock.

        # Iteratring over the list until we reached our max profit.
        while right < len(prices):
            # Ensures the current profit is postive.
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                # Get our max profit from that right's iteration.
                max_profit = max(max_profit, profit)
            else:
                left = right # We want to buy at the lowest price.
            right += 1 # We check all the places we want to sell.

        return max_profit

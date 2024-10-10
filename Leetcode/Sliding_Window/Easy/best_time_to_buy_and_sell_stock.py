'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # start at 0 and 1 index because you must buy before you sell
        l, r = 0, 1
        # answer that we want to maximize (what information we want to take away from having this window)
        max_profit = 0
        while (r < len(prices)):
            # This is the window integrity: in this case, we have a profit (YAY) and want to check if this yields more profit
            if (prices[l] < prices[r]):
                max_profit = max(max_profit, prices[r] - prices[l])
            # This is the window integrity: in this case, we want a profit, we only get a loss if the sell price is lower than the buy price
            # What this also means is that there is a new lowest value that we could have bought to better potentially maximize our sell price    
            else:
                # Shrink window so that integrity is valid
                l = r
            # Expand our window
            r += 1
        return max_profit
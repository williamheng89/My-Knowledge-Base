'''
The Sliding Window algorithm is a technique used to efficiently solve problems that involve finding a subrange (or window) of elements in an array or list. 
Instead of recomputing values for overlapping sections of the array, we maintain a subset (window) of elements and slide this window across the array, 
    updating the result in constant time by adding new elements and removing old ones as the window moves.

How It Works:
Window Initialization: Start by defining a window of size k (or a dynamic size, depending on the problem) at the beginning of the array.

Move the Window: Slide this window one element at a time. Each time you slide:

Remove the element that is leaving the window (leftmost element).
Add the element that is entering the window (next element in the array).
Update the Result: After each slide, update the result based on the current window (e.g., sum, maximum, minimum, etc.), 
    Ensure WINDOW INTEGRITY: shift window until the window contents are valid

Repeat: Continue sliding the window until you've processed the entire array.

By moving the window one step at a time, we can solve problems that would otherwise require recalculating results for each subset of elements, which could be inefficient.
'''

def longestWindow(nums: List[int]) -> int:
    j = 0, ans
    for i in range(nums):
        # code using nums[i] to update the state 
        # that might invalidate the window
        while invalid():
            # code using nums[j] to update the state
            # and shrink the left edge while the window is invalid
            j += 1
        # longest window so far = len([i, j])
        ans = max(ans, i - j + 1); 
    
    return ans

'''
Example:

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
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
'''
https://leetcode.com/problems/house-robber/
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Tabulation Approach
        memo = [0] * len(nums)
        # Set up base cases:

        # Most profit made while having options to just house 0 is house 0's value
        memo[0] = nums[0]
        if len(nums) == 1:
            return  memo[0]
        # Most profit made while while having options to house 1 and house 0 is the max of one
        memo[1] = max(nums[0], nums[1])
        if len(nums) == 2:
            return memo[1]
        
        # Now we look at house 2 and beyond
        for i in range(2, len(nums)):
            # Most profit made while at house i is the most including this one (but that means you CANNOT have robbed the previous), or
            # Most profit made while at house i is the most excluding this one (but that means you COULD have robbed the previous)
            memo[i] = max(nums[i] + memo[i-2], memo[i-1])
        #  We have built a tabulation of most profit given a house index
        return memo[len(nums)-1]
       
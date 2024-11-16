'''
https://leetcode.com/problems/monotonic-array/
'''
class Solution:
    '''
    Goal:
    We want to check if an array is monotonically increasing or decreasing. If either, return true, else false
    
    A monotonic array is one that starting from the first index to the last, all items are either increasing (increasing monotonic array) or decerasing (a decreasing one)
    
    Plan:
    
    Knowing this, all we need to do is read over the array. Because we only care that it is either increasing or decreasing, we can just set 2 flags (to track for either types) and then proceed to iterate through the array. We compare the element of index i with element of i + 1. To handle the condition that all items are the same value, this is technically a valid monotonically increasing or decreasing depending on the previous categorization of the array because it is all inclusive.
    '''
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        decreasing = True
        increasing = True
        
        for i in range(len(nums) - 1):
            if (nums[i] > nums[i+1]):
                increasing = False
            if (nums[i] < nums[i+1]):
                decreasing = False
        return decreasing or increasing
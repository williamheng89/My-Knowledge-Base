'''
https://leetcode.com/problems/two-sum/
'''
class Solution(object):
    '''
    - Straight forward
    - use hashmap to keeptrack of value and index
    - iterate through the numbers and see what the difference between current index value and goal is
    - if 'difference' value is in the hashmap, you have solution, return (index of difference, current index) 
    '''
    def twoSum(self, nums, target):
        hash_map = {}
        difference = 0
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            difference = target - nums[i]
            if (difference in hash_map):
                return hash_map[difference], i
            if (nums[i] not in hash_map):
                hash_map[nums[i]] = i
        return 0, 0
        
        
        
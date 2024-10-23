'''
https://leetcode.com/problems/longest-consecutive-sequence/
'''
class Solution(object):
    '''
    - Straight forward
    - Add all elements into a set
    - For all elements in the set, check for element + 1 (next in the sequence) until no more
    '''
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        num_set = set()
        
        for n in nums:
            num_set.add(n)
        
        for n in nums:
            if (n-1) not in num_set:
                length = 1
                while (length + n) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest
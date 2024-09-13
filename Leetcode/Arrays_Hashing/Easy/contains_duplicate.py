'''
https://leetcode.com/problems/contains-duplicate/
'''
class Solution(object):
    '''
    - Straight forward
    - Keep a set of letters
    - Traverse and check if each letter is inside the set or not
    '''
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        my_set = set()
        for n in nums:
            if (n in my_set):
                return True
            else:
                my_set.add(n)
        return False
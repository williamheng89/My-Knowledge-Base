'''
https://leetcode.com/problems/group-anagrams/
'''
class Solution(object):
    '''
    - Straight forward, same as valid anagram
    - Now you need to group anagrams by making the list of letter counts into a tuple (cannot hash lists)
    - if the tuple of letter frequencies are not new, there is already a group out there and you append to that group
    '''
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        to_return = {}
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            if (key not in to_return):
                to_return[key] = [s]
            else:
                to_return[key].append(s)
        return to_return.values()
            
            
        
        
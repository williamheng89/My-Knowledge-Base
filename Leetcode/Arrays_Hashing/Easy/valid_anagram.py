
'''
https://leetcode.com/problems/valid-anagram/
'''
class Solution(object):
    '''
    - Straight forward
    - create 2 arrays, each of len 26 for length of alphabet
    - increment count (the index of the array is the letter)
    - traverse through both arrays and see if counts are the same
    '''
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_list = [0]*26
        t_list = [0]*26
        for i in range(len(s)):
            s_list[ord(s[i])-ord('a')] += 1
            t_list[ord(t[i])-ord('a')] += 1
        for i in range(len(s_list)):
            if (s_list[i] != t_list[i]):
                return False
        return True

        
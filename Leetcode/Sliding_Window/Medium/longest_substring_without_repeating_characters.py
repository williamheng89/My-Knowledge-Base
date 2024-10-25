class Solution(object):
    '''
    Goal: Find the length of the longest substring that contains no duplicate characters
    
    Idea:
    
    - Create a sliding window (within this window, we must uphold the condition that there is no duplicate characters)
    - We do this by creating a window using left and right pointers
    - We iterate over the string (expanding our window) --> take the max at every step
    - We keep a growing hashset.
    - Once we find a duplicate, while we are that that duplicated character, we remove all characters starting from the left pointer towards the right pointer
    - We check by seeing if its in the hashset.
    - Thus we are shrinking our sliding window until the condition (no duplicate characters can be contained in this) is upheld again
    '''
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        hashset = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            longest = max(longest, r - l + 1)
        return longest            
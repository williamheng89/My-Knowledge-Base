'''
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
'''
class Solution:
    '''
    Goal: Given a string s, we want find the maximum number of vowel letters in any substring of length k
        in other words: we have a window of length 5 and we find the most vowels that can appear in that window as we screen through the entire string
        
    Plan: This is a sliding window problem
    
    We know this is a sliding window problem because we care about finding information on ranges of values within an array.
    
    Brute force approach:
        We can start at every index within the string, and check for the next k (inclusive) characters and keep track of the maximum number of vowels we see.
        
    Optimized approach:
        We cna create a window of size k first starting at 0 up until k-1 and find out the number of vowels inside.
        Then we will drag the window through the string by incrementing the left and right pointers.
        We then just need to track what goes in and what leaves to understand the contents inside of the window.
        
        At every increment, we can just take the maximum.
    '''
    def maxVowels(self, s: str, k: int) -> int:
        
        max_vowels = 0
        count = 0
        vowels = set(['a', 'e', 'i', 'o', 'u',])
        l, r = 0, 0
        
        while (r < k):
            if s[r] in vowels:
                count += 1
            r += 1
            
        max_vowels = max(max_vowels, count)
        
        for r in range(r, len(s)):
            if s[r] in vowels:
                count += 1
            if (s[l] in vowels):
                count -= 1
            l += 1
            max_vowels = max(max_vowels, count)
        
        return max_vowels
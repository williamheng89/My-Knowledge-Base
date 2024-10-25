class Solution(object):
    '''
    Goal: Given string s and integer k, find the length of the longest substring of 
        repeating characters, s.t. you can make k replacements

    How: This calls for a sliding window because we are trying to highlight a property of contiguous elements
    - In this case, we want to find a subsequence of repeating charcters

    To do so, we need create a sliding window, and ensure its validity --> what will the window highlight and what makes it valid?

    Window condition: (While the window is invalid...):
        (The size of the window) - (highest frequency of a character inside the window) <= k
        This is because the difference of these two numbers reveals how many characters you need to replace
        If this exceeds k, that means you need to replace more than k and thus the window is invalid

    Ensuring valiidity: (While the window is invalid): Do...
        We simply need to decrement the frequency of the character at the left pointer and move the pointer to the right
        until the window is then valid
    '''
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Set up list to track letter frequencies
        freq = [0] * 26
        # Set up left pointer
        left = 0
        # Set up tracker for longest measurement
        longest = 0
        # Sliding Window
        for right in range(len(s)):
            freq[ord(s[right]) - ord('A')] += 1
            most_freq = max(freq)
            # Window condition: fix the window if (size of window) - most frequent character in the window > k --> this means need to replace more than k
            while (right - left + 1 - most_freq > k):
                # Shrink the window by moving left pointer (this also means to adjust what the window contents are --> decrease the frequency count)
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            # Window is valid now, measure the window 
            longest = max(longest, right - left + 1)
        return longest
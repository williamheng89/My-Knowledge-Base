'''
https://leetcode.com/problems/sliding-window-maximum/
'''
class Solution(object):
    '''
    Goal: We are going to have a window of size k. We will then drag this window through
        all the positions starting at 0 till the end. At every move to the right, we want to know the largest number within that sliding window
        
    Plan:
        We will be creating a sliding window (because we need to know what goes in
        and also what goes out). We will also be needing to track what the largest element
        within the sliding window is as well as what will be the next largest item when it
        gets kicked out (we do not want to have to O(n) iterate through the entire sliding
        window to calculate the largest element after shifting the window to the right)
        
    We need a res array, left and right pointers, a variable to track what the current
    largest number in the sliding window is, and a queue (deque).
    
    We will be designing the queue to be monotonically decreasing (the front of the queue 
    will be the largest number and all proceeding numbers will be decreasingly less)
    
    We need to have it designed this way because as the sliding window shifts to the right,
    an element will be kicked out (if this is the largest number in the window, we need to 
    immediately know what the next one is). When this happens, we can just pop the leftmost 
    item from the queue, and the next element will be the largest.
    
    To make a queue monotonically decreasing:
        Everytime the right pointer moves (when we shift the sliding window) we check if
        the newly introduced item is bigger than the item at the end of the queue, if so,
        we contionuously pop until it isn't and then append this item to the queue. 
    
    With this monotinically decreasing designed queue, once an item is kicked out of the 
    window, we simply need to pop from the left and the largest element is the new head.
    
    To get things set up, I performed this on the first initial window [0, k -1]
        
    '''
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        left = 0
        max_val_window = float('-inf')
        queue = deque([max_val_window])
        
        for i in range(left, k):
            while queue and (nums[i] > queue[-1]):
                queue.pop()
            queue.append(nums[i])
        max_val_window = queue[0]
        res.append(max_val_window)
        
        right = k - 1
        right += 1
        
        while (right < len(nums)):
            if nums[left] == max_val_window:
                queue.popleft()
            left += 1
            
            while queue and (nums[right] > queue[-1]):
                queue.pop()
            queue.append(nums[right])
            max_val_window = queue[0]
            res.append(max_val_window)
            right += 1
        return res
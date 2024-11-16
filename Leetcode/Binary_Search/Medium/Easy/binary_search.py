'''
https://leetcode.com/problems/binary-search/
'''
class Solution:
    '''
    Goal: We are given a sorted array of integers (ascending). We wnat ot search for a target number. In order to do so, we want to have an O(log n) runtime -- done via binary serach. Thus we need to implement a binary search
    
    Plan:
    
    What does a bianry search need?
    
    - 2 pointers (the ends of the window)
    - a pointer for the middle of the window
    - set the edge pointers to the middle pointer (shrink the window) until middle == target
    
    '''
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid  # target found
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
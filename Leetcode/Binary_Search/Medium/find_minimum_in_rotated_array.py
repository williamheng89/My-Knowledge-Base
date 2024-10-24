'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''
class Solution(object):
    '''
    Binary Search allows us to divide the array and look at halves.

    - if nums[left] <= nums[pivot], this means that everything to the left of pivot point is already sorted
        - Thus we continue the search in the right half
    - if not, this means the inflection is somewhere within the left side
        - Thus we continue the search in the left half
    '''
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        smallest = float('inf')
        
        while (left <= right):
            if (nums[left] <= nums[right]):
                smallest = min(smallest, nums[left])
                break
                
            pivot = (left + right) // 2
            
            smallest = min(smallest, nums[pivot])
                
            if (nums[left] <= nums[pivot]):
                left = pivot + 1
            else:
                right = pivot - 1
        return smallest
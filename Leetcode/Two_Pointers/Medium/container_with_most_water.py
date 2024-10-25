'''
https://leetcode.com/problems/container-with-most-water/
'''
class Solution(object):
    '''
    Goal: volume = min(shortest height) * width

    - Have 2 pointers at both ends
    - Find volume
    - Want to maxmize so if the right side is biggest, move the left towards the right,
        if left side is the biggest, move the right side towards the left
    '''
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l = 0
        r = len(height)-1
        while (l != r):
            product = min(height[l], height[r]) * (r - l)
            res = max(product, res)
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return res    
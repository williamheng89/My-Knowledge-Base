'''
https://leetcode.com/problems/same-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    Goal: Given two roots (p, q) of 2 trees, check if they are the same

    Base Cases:
    - If both roots are null --> they are the same --> ret True
    - If only one is --> the are not the same --> ret False
    - If the value of each root is different --> they are not the same --> ret False

    Recursive Case:
    - Recurse on left side of both p and q, recurse on right side of p and q
    '''
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
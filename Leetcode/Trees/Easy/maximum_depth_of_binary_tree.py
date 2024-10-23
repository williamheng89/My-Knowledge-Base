'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    Goal: Find the maximum depth of a binary tree (the number of nodes along the longest path)
        starting from root until leaf node

    Base Case:
    - root = Null --> height is 0 (ensures depth of 0 for empty tree)

    Recursive Case:
    - calculate the maximum depth of the left and right subtrees of current node (recurse)
    - add 1 to account for the depth of current node
    '''
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)
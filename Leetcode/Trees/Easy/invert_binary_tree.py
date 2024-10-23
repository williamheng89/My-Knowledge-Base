'''
https://leetcode.com/problems/invert-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    Goal: Swap every node's left child with its right child
    
    Base Case:
    - root is null --> just return it

    Recursive Case:
    - Swap left and right children
    - Recurse on left and right children
    '''
    def invertTree(self, root):    
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if (root == None):
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
'''
https://leetcode.com/problems/subtree-of-another-tree/
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    Goal: Check if a tree is a subtree in another tree

    Base Case:
    - If subRoot == None --> it is a subtree because its the same as any leaf node
    - If subRoot is not None but root is --> this is not a subtree 

    Recursive Case:
    - Can make use of similar problem (Is Same Tree)
    - Check if any node in root is the same as subRoot
    '''
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        #######################################################
        def isSameTree(root1, root2):
            if root1 == None and root2 == None:
                return True
            elif root1 == None or root2 == None:
                return False
            elif root1.val != root2.val:
                return False
            else:
                return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        #######################################################
        
            
        if subRoot == None:
            return True
        elif root == None:
            return False
        
        if (isSameTree(root, subRoot)):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
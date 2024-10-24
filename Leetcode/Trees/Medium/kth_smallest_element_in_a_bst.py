# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    Goal: perform inOrderTraversal --> store into array --> return arr[k-1]
    '''
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        ##############################################
        def inOrderTraversal(stack, node):
            if node == None:
                return

            inOrderTraversal(stack, node.left)
            stack.append(node.val)
            inOrderTraversal(stack, node.right)

            return stack
        ##############################################

        
        stack = []
        stack = inOrderTraversal(stack, root)
        
        return stack[k - 1]
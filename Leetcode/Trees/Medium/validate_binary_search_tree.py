# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    Goal: Given a root, validate that the tree is a BST
    Sub problems (for all nodes):
    - node.left.val < node.val < node.right.val
    - Its children must also follow these rules s.t. 
        - node.left.children's.val < node.val and node.val < node.right.children's.val
        - Can ensure this by tracking valid values
            - At the root, it's value can be between -inf and +inf
            - root's left child value can be between -inf and root.value
            - root's right child value can be between root.value and +inf
            - --> continue with this as you go down 

    Base Case:
    - If root == None --> this is valid
    - If not left_val < curr_val < right_val --> invalid

    Recursive Case:
    - Validate the left by placing limit that left value must be less than current value but
        greater than the left limit
    - Validate the right by placing limit that right value must be greater than current value but
        less than the right limit
    '''
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(root, left_val, right_val):
            if root == None:
                return True
            if (left_val < root.val) and (root.val < right_val):
                return validate(root.left, left_val, root.val) and validate(root.right, root.val, right_val)
            else:
                return False         
            
            
        return validate(root, -float('inf'), float('inf'))
        
           
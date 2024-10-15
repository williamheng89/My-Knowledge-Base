'''
        4
       / \
      2   6
     / \ / \
    1  3 5  7
'''

'''
TRAVERSALS
'''

# Pre-order Traversal: Root -> Left -> Right
def pre_order_traversal(node):
    if node:
        # Visit the root (current node)
        print(node.value, end=" ")
        # Traverse the left subtree
        pre_order_traversal(node.left)
        # Traverse the right subtree
        pre_order_traversal(node.right)
# OUTPUT: 4 2 1 3 6 5 7

# Pre-order Traversal: Left -> Root --> Right
def in_order_traversal(node):
    if node:
        # Traverse the left subtree
        in_order_traversal(node.left)
        # Visit the root (current node)
        print(node.value, end=" ")
        # Traverse the right subtree
        in_order_traversal(node.right)
# OUTPUT: 1 2 3 4 5 6 7

# Post-order Traversal: Left --> Right --> Root
def post_order_traversal(node):
    if node:
        # Traverse the left subtree
        in_order_traversal(node.left)
        # Traverse the right subtree
        in_order_traversal(node.right)
        # Visit the root (current node)
        print(node.value, end=" ")
# OUTPUT: 1 3 2 5 7 6 4

'''
SEARCHING
'''

# BFS (Level-order Traversal)
def bfs_traversal(root):
    if root is None:
        return
    
    # Use a queue to ensure FIFO
    queue = deque([root])
    
    while queue:
        # Dequeue the front node
        node = queue.popleft()
        # Visit the node
        print(node.value, end=" ")
        
        # Enqueue left child
        if node.left:
            queue.append(node.left)
        # Enqueue right child
        if node.right:
            queue.append(node.right)

# DFS (Depth-First Search) using a stack
def dfs_traversal(root):
    if root is None:
        return
    
    # Use a stack to ensure LIFO
    stack = [root]
    
    while stack:
        # Pop the top node
        node = stack.pop()
        # Visit the node
        print(node.value, end=" ")
        
        # Push left child        
        if node.right:
            stack.append(node.right)
        # Push right child
        if node.left:
            stack.append(node.left)
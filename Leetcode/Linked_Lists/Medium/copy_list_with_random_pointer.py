'''
https://leetcode.com/problems/copy-list-with-random-pointer/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    '''
    Goal: We are given the head of a linked list. Within this Node class, each node has fields for: value, next node, and a random node (This is the index within the linked list of nodes).
    
    We want to create a deep copy, such that we create n new nodes and every new nodes' fields are the same as those described in the original.
    
    Plan:
    
    We can do a 2 pass. In the first pass, create a map for that maps old_node to new_node
    
    on second pass, change new_node's next and random fields to mapped old_node's data.
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        node_map = {None: None}
        # node_index = {}
        
        current_node = head
        index = 0
        
        while (current_node != None):
            # node_index[current_node] = index
            node_map[current_node] = Node(current_node.val)
            
            # index += 1
            current_node = current_node.next
        
        current_node = head
        
        while (current_node != None):
            
            node_map[current_node].next = node_map[current_node.next]
            node_map[current_node].random = node_map[current_node.random]
            
            current_node = current_node.next
        
        return node_map[head]
'''
https://leetcode.com/problems/clone-graph/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    '''
    Goal: Given a node (val, neighbors[]) -- lookup/ manipulate with val, create a deep copy. -->
    
    Given a node (val, neights[]) we want to perform a wide spread search through every node's set of neighbors, create deep copies of each new node, and hook them up to their respective neighbors in the original graph.
    
    Plan:
    
    (What DS/A do we need?) 
    
    - Need to perfom some kind of search throughout each node's neighbors -- BFS
        - Need a queue
    - Create new nodes and keep track of node relationships:
        - have some sort of set? s.t. if we have not seen a node listed in some node's neighbors, we make one and put it in the hashset 
        (maps reference node to new node -- deep copy)
    
    
    Cautions:
    queue will contain references to the original graph
    
    hashset will map [original node reference] --> new deep copy of node
    '''
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if (node == None):
            return None
        
        queue = collections.deque()
        queue.append(node)
        
        node_set = {}
        node_set[node] = Node(node.val)
        
        while (len(queue) > 0):
            current_node = queue.popleft()
            
            for neighbor in current_node.neighbors:
                if neighbor not in node_set:
                    node_set[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                node_set[current_node].neighbors.append(node_set[neighbor])
                
        return node_set[node]
                    
                
        
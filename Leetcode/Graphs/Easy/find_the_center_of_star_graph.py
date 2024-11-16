'''
https://leetcode.com/problems/find-center-of-star-graph/
'''
class Solution:
    '''
    Goal: We are given a list that contains elements of [a,b] such that the element represents a edge between nodes a and b, find the center of the star graph
    
    Plan: Essentialy how do we define the center of the graph? The center of the graph is the node that has the most edges
    
    Thus we simply need to track which node has the most amount of connections (edges) and return the value of the node.
    
    To help with this, we can use a hashmap because we can track to see if we have seen that node before as well as map it to a counter that tracks how many connections (neighbors) it has. 
    
    We can then just iterate through the map, find the node with the highest amount of neigbors and return that node.
    '''
    def findCenter(self, edges: List[List[int]]) -> int:
        connections = {}
        max_connections = 0
        center = 0
        
        for node1, node2 in edges:
            if node1 not in connections:
                connections[node1] = 1
            else:
                connections[node1] += 1
            
            if node2 not in connections:
                connections[node2] = 1
            else:
                connections[node2] += 1
        
        for key, value in connections.items():
            if value > max_connections:
                max_connections = value
                center = key
                
        return center
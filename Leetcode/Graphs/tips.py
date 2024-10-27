'''
Tips to Solve: https://leetcode.com/discuss/study-guide/3835684/Mastering-Graph-Problems%3A-A-Step-by-Step-Guide 

1. Understand the Problem:
Begin by thoroughly understanding the problem statement. 
    Identify the type of graph (directed or undirected) and any constraints imposed. Ask yourself questions like:


- What are the nodes and edges representing?
- Are there any special nodes (e.g., start, end, etc.)?
- What is the expected output format?

2. Choose the Appropriate Graph Representation:
Select a suitable data structure to represent the graph. 

- Adjacency Matrix: A 2D array where matrix[i][j] indicates the presence of an edge between node i and j.
- Adjacency List: A dictionary or array of lists, where each node is mapped to its neighboring nodes.

3. Choose the Right Graph Traversal Technique:
Common graph traversal techniques include:


- Breadth-First Search (BFS): Use a queue to explore nodes level by level.
- Depth-First Search (DFS): Use recursion or a stack to explore nodes as deeply as possible before backtracking.
- Dijkstra's Algorithm: Find the shortest path in weighted graphs with non-negative edge weights.
- Bellman-Ford Algorithm: Find the shortest path in weighted graphs with negative edge weights.
- A* Algorithm: An informed search algorithm that uses heuristics to prioritize exploration towards the goal.

4. Practice Backtracking (For DFS):
If your problem requires exhaustive search, practice backtracking techniques to efficiently explore all possible paths in the graph. 
    Memoization can significantly improve performance by avoiding redundant computations.

5. Detect Cycles (For Cyclic Graphs):
If the graph can contain cycles, develop a cycle detection mechanism. 
    For instance, you can use DFS to check for back edges or maintain a visited set to track visited nodes during traversal.
'''

# For when you have a m x n matrix and want to do a BFS starting at a specific location
# This works for 4-directional and avoids "obstacles"
# Will return a set of cells you were able to visit, based on the critera that you want to visit cells whose value='1'

def BFS(self, grid, x, y):
        # Initialize a queue
        queue = deque()
        # Track which locations you have seen
        visited = set()
        # Get Boundaries
        m, n = len(grid), len(grid[0])
        # Create directions of exploration
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

        # Add this location to the queue to initiate BFS
        queue.append((x, y))
        # Mark cell as visited
        visited.add((x, y))  

        # Explore for as long as you are able to reach
        while len(queue) != 0:
            # Pop from queue and remove from set (you've now explored this piece)
            i, j = queue.popleft()

            # exploration
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                # How?
                # Check if directions are within boundaries.
                # Check if direction to explore to is land (we don't care about water)
                # Check if we've direction to explore in has already been explored or is already in the frontier
                if (0 <= new_i < m) and (0 <= new_j < n) and (grid[new_i][new_j] == '1') and ((new_i, new_j) not in visited):
                    # add to frontier
                    queue.append((new_i, new_j))
                    visited.add((new_i, new_j))
        return visited
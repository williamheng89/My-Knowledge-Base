'''
https://leetcode.com/problems/number-of-islands/
'''
class Solution(object):
    '''
    Goal: Given an m x n matrix of "0": water, and "1": land, 
        find the number of islands 

    How: Put all "land" pieces into a set, perform a BFS on all land pieces,
    - The number of times you perform BFS is the number of islands

    Slight spatial complexity optimization: we don't need "visited" set, can just check if direction to explore in is already in the queue or not
    '''
    ###########################################################
    def BFS(self, known_land, grid, x, y):
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
            known_land.remove((i, j))

            # exploration
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                # How?
                # Check if directions are within boundaries.
                # Check if direction to explore to is land (we don't care about water)
                # Check if we've direction to explore in has already been explored or is already in the frontier
                if (0 <= new_i < m) and (0 <= new_j < n) and (grid[new_i][new_j] == '1') and ((new_i, new_j) in known_land) and ((new_i, new_j) not in visited):
                    # add to frontier
                    queue.append((new_i, new_j))
                    visited.add((new_i, new_j))
        return known_land
    ###########################################################
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Set up
        land = set()
        num_islands = 0

        # Adding cells of land
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':  # found land
                    land.add((i, j))

        # Finding number of islands
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # everytime we enter this condition/ BFS, we know there was no way to get to this land, therefor this mass is an island
                if (i, j) in land:
                    # Shrink the number of land cells "explored already"
                    land = self.BFS(land, grid, i, j)
                    num_islands += 1
        return num_islands


                
    
    
            
        
        
'''
https://leetcode.com/problems/pacific-atlantic-water-flow/
'''
class Solution:
    '''
    Goal: 
        Given an  m x n grid, this represents the heights on an island. 
        Beyond the top of the grid and the left side of the grid is the Pacific Ocean. 
        Beyond the right side of the grid and bottom of the grid is hte Atlantic Ocean.
        
        As the island has varing heights, rain water can trickle down to lower heights.
        We want to find the zones such that rain can trickle down into both the Pacific Ocean and the Atlantic Ocean
        
    Plan:
        We can do a brute force approach. We can review every single cell in this grid and check that moving in the 4 directions, we can reach the edge of the grid.
        
        This will work but is quite inefficient because we are checking every cell against every other cell which is O(m*n)^2
        
        The better approach is that we know all the cells along the north and west edges already meet the Pacific ocean.
        And all cells along the east and south edges already meet the Atlantic ocean.
        
        I think we can just start at these cells and DFS towards the middle (from the edges). This is because all the outer edges we are already at the ocean.
        If we expand towards the center and make sure that the cells we visit are of greater heights than the previous, that means that those cells can make to the edges as well (water flows from greater highest to lower)
        
        So we can probably keep track of how far the DFS can strecth for both the Pacific and Atlantic ocean cells (edges) and to find the cells that can flow into both, we return the sells that are in both containers of Pacific and Atlantic DS. (set)
        
        Time Notation:
        
        This takes O(m*n) because we will be doing a DFS on each cell which means that each cell will be visited once in the worst case. 
        Since we will be performing for both the Atlantic and Pacific Ocean cells, we do this 2 times O(2*m*n) = O(m*n). Each DFS operation takes only O(1).
    
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])
        
        pacific_ocean_reach_cells = set()
        atlantic_ocean_reach_cells = set()
        
        def dfs (r, c, visited, previous_height):
            if (r < 0 or c < 0 or 
                r == rows or c == columns or
                (r, c) in visited or
                heights[r][c] < previous_height):
                
                return
            
            visited.add((r,c))
            
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            
        for c in range(columns):
            dfs(0, c, pacific_ocean_reach_cells, heights[0][c])
            dfs(rows - 1, c, atlantic_ocean_reach_cells, heights[rows - 1][c])
            
        for r in range(rows):
            dfs(r, 0, pacific_ocean_reach_cells, heights[r][0])
            dfs(r, columns - 1, atlantic_ocean_reach_cells, heights[r][columns-1])
            
        res = []
        
        for r in range(rows):
            for c in range(columns):
                if ((r,c) in pacific_ocean_reach_cells and
                    (r,c) in atlantic_ocean_reach_cells):
                    
                    res.append((r,c))
                    
        return res
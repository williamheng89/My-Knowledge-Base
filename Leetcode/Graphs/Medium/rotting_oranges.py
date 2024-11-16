'''
https://leetcode.com/problems/rotting-oranges/
'''
class Solution:
    '''
    Goal: We have an m x n grid where each cell has either a 0, 1, 2 signifying empty, fresh orange, and rotten orange. We want to find how long it takes for the rotten oranges to infect all the fresh oranges (if it is even possible). Every minute, if a fresh orange is adjacent (horizontally or vertically) to an infected orange, it becomes rotten i.e. if a rotten on is by a fresh one, the fresh one becomes rotten.
    
    Plan:
    
    Perform some sort of BFS?
        - conditions to expand:
            - Start at a rotten orange
            - if rotten orange is adjacent to a fresh one, it will infect that one
            - empty spaces don't matter
            - keep track of those we visited
    DS/A:
    
        - BFS needs a queue
        - keep track of the bounds of where we can search
        - track those that are fresh
        - track those that are rotten
        - track the time
        
    
    
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        
        queue = collections.deque()
        
        fresh = 0
        time = 0
        
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    queue.append((row,column))
                elif grid[row][column] == 1:
                    fresh += 1
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while len(queue) > 0 and fresh > 0:
            # break the BFS into layers that grow outwards. Each layer represents 1 minute
            size_of_bfs = len(queue)
            for i in range(size_of_bfs):
                r, c = queue.popleft()
                
                for direction_row, direction_column in directions:
                    row = r + direction_row
                    column = c + direction_column
                    
                    # Simply track those infected by only enacting on fresh oranges
                    if (row in range(rows) and column in range(columns) and
                        grid[row][column] == 1):
                        
                        fresh -= 1
                        grid[row][column] = 2
                        queue.append((row, column))
                
            time += 1
        if fresh != 0:
            return -1
        else:
            return time
                        
                
            
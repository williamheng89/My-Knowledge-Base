'''
https://leetcode.com/problems/surrounded-regions/
'''
class Solution:
    '''
    Goal: We are given an m x n grid (board) whose cell contents are 'X', 'O'.
    
    Cells are connected horizaontally and vertially (4 directions). 
    
    A region is defined with 'O', it it is neigherboring other 'O's they are a bigger region
    
    We can surround 'O's with 'X' such that none of the region cells are on the edges. 
    
    So basically we will be having bodies of regions 'O' and we can surround them when they are isolated away from the edges (the body is not on an edge)
    
    Plan:
    
    We should iterate throughout the entire grid, and make a set() to track there the 'O's are. 
    We should also create a set() that will track what cells we have visited. This is because we will be iterating over all 'O' cells and performing a BFS on each of these cells such that for every cell we start at, we will explore until we explore the entire body (region of 'O's), and if any part of this region lays on an edge -- we may not squeez and surround this region. Else we can. -- if at the end of our BFS we did not land on an edge, we can make all of these 'O's into n 'X'
    
    Our set of visited cells will make sure we do not do duplicate work    
    '''
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
            
        # Set up variables and sets
        
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        rows = len(board)
        columns = len(board[0])
        
        region_set = set()
        visited_cells = set()                
        
        # fill up set that tracks where the 'O's are
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == 'O':
                    region_set.add((r,c))
                    
        
        
        for (r, c) in region_set:     
            if (r,c) in visited_cells:
                continue
                
            on_edge = 0
            visited_group = set()
            queue = collections.deque([(r,c)])
            while (len(queue) > 0):
                row, column = queue.popleft()
                if (row < 0 or column < 0 or
                    row == rows or column == columns or
                    board[row][column] == 'X' or
                    (row, column) in visited_group or
                    (row, column) in visited_cells):

                    continue
                    
                visited_group.add((row,column))
                visited_cells.add((row,column))
                if (row == 0 or row == rows - 1 or
                    column == 0 or column == columns - 1):
                    
                    on_edge = 1 
                queue.append((row + 1, column))
                queue.append((row - 1, column))
                queue.append((row, column + 1))
                queue.append((row, column - 1))
                
            if (on_edge == 0):
                for (row_remove, col_remove) in visited_group:
                    board[row_remove][col_remove] = 'X'
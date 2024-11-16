'''
https://leetcode.com/problems/word-search/
'''
class Solution:
    '''
    Goal: We want to seach a grid to see it it contains a string. In order for a string to be valid within the grid is that the letters must be from adjacent cells (vertically or horizontally) and a cell may not be reused.
    
    Plan:
    This calls for some form of DFS because we want to search as deep as we can to see if a string is present in the grid. Traversing through the grid is fairly simple, we just need to move in 4 directions (up, down, left, right) while making sure that the cells we visit are not out of bounds, not previously visited from the current path, and that since we know the contents of the string, the cells we search must be relevant to the character we are trying to find. Knowing all of this, we perform a DFS at every cell within the grid, and recurse to search as deep as we can every time.
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        
        path = set()
        
        def dfs(row, column, index):
            if index == len(word):
                return True
            
            if (row < 0 or column < 0 or 
                row >= rows or column >= columns or
                board[row][column] != word[index]
                or (row, column) in path):
                return False
            
            path.add((row, column))
            
            res = (dfs(row + 1, column, index + 1) or
                    dfs(row, column + 1, index + 1) or
                    dfs(row - 1, column, index + 1) or
                    dfs(row, column - 1, index + 1))
            
            path.remove((row, column))
            
            return res
        for row in range(rows):
            for column in range(columns):
                if dfs(row, column, 0) == True:
                    return True
        return False
        
'''
https://leetcode.com/problems/valid-sudoku/
'''
class Solution(object):
    '''
    I think this problem isn't difficult but is tedious, and forces you to 
    understand how to use arrays and sets.

    My approach is to essentially perform checks along every horizontal, every 
    vertical, and then within every 3x3 square. 

    This problem forces you to know how to index through a 2-D array.
    '''
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, 9):
            check = set()
            for j in range(0, 9):
                if (board[i][j] == "."):
                    continue
                if (board[i][j] not in check):
                    check.add(board[i][j])
                else:
                    return False
            check.clear()
        
        for i in range(0, 9):
            check = set()
            for j in range(0, 9):
                if (board[j][i] == "."):
                    continue
                if (board[j][i] not in check):
                    check.add(board[j][i])
                else:
                    return False
            check.clear()
                
        for i in range(0, 9, 3):
            check = set()
            for j in range(0, 9, 3):
                for k in range(0, 3):
                    for l in range(0, 3):
                        if (board[i+k][j+l] == "."):
                            continue
                        if (board[i+k][j+l] not in check):
                            check.add(board[i+k][j+l])
                        else:
                            return False
                check.clear()
        return True


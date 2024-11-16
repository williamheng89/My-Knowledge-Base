'''
https://leetcode.com/problems/letter-case-permutation/
'''
class Solution:
    '''
    Goal: We are given a string of letters and numbers. We want to find all the possible strings such that the letters can be individually uppercased and lowercased.
    
    Plan:
    
    When I hear "all the possible ..." I think of brute force searches and DFS because we are exploring as deep and far as we can before we backtrack.
    
    As we see that for each character, if its a letter we want ot explore 2 decisions (uppercase and lowercase), but if it is a digit, we just explore as is 
    
    We can develop a recursive function: dfs(index, state)
        Base Case: when the index is equal to the string length, we have a viable solution
        
        Recursive Cases: branch if necessary (alphabetical characters vs digits). And we will be accumulating characters to our state[].
        
        Time Complexity is O(2^n) where n is the number of letters as each letter we create 2 decision paths.
    '''
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
                
        def dfs(index, state):
            if index >= len(s):
                res.append("".join(state))
                return
            
            if s[index].isalpha():
                dfs(index + 1, state + [s[index].lower()])

                dfs(index + 1, state + [s[index].upper()])
            else:
                dfs(index+1, state + [s[index]])
                
        dfs(0, [])
        
        return res
        
        
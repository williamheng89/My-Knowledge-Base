'''
https://leetcode.com/problems/combination-sum/
'''
class Solution:
    '''
    Goal: We want to find unique combinations of numbers to equal a target goal. We are allowed to reuse numbers an unlimited number of times. However each combination must be unique.
    
    Plan: 
    
    Initially we may want to just brute force and try every single combination.  However this will lead to issues with combinations not being unique.  For example given the example input of candidates = [2,3,6,7] and target = 7, we can have [2, 2, 3], [2, 3, 2], as successful combinations if we were to just iterate over each number and give access to the entirety of candidates[] to choose from, but this will lead to non-unique combinations. 
    
    Thus our approach needs to limit access to which candidates can be added into our combinations. 
    
    We can achieve this by doing a DFS such that we make 2 decisions: include this candidate, add it to our state, and continue recursing; or do not include this candidate, do not add it to our state, and continue recursing. Thus on one side of our decision tree and using the provided example candidates, all children will have a 2 and on the other side of the decision, no children will have a 2. Then within the next level, we can have all children with 2 2s and all children with only 1 2 and so on so forth.
    
                            []
                /                           \
            [2]                             []
        /       \                       /       \
    [2,2]       [2]                 [3]         []
    /   \       /   \               /   \       /   \
[2,2,2] [2,2]  [2,3] [2]          [3,3]   [3]    [6]  []
/       / \      / \   /\          / \    / \    /  \  /  \
8 [2,2,3] [2,2] [2,3,6] 8 9  [3,3,3][3,3] 9            [7]

The decision will look something like this. As you can see, we will not have duplicates due to properties that candidates are distinct and our mechanism of each decision either including taking a number (adding it to our sequence) or completely not taking it ever again.
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, state, total):
            if total == target:
                res.append(state.copy())
                return
            if index >= len(candidates) or total > target:
                return
            
            state.append(candidates[index])
            dfs(index, state, total + candidates[index])
            
            state.pop()
            dfs(index + 1, state, total)
            
        dfs(0, [], 0)
        return res
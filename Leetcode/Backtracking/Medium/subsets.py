class Solution:
    '''
        Goal: We want to find all the subsets of a list of numbers --> these are not permutations
        
        Plan:
        We can think of this problem as a massive decision tree.
        
        Given an example of array [1,2,3]
        
        we can start with an empty array (our subset to append to result) and begin making decisions from index 0
        
                            []
                /                           \
            [1]                             []
        /       \                       /       \
    [1,2]       [1]                 [2]         []
    /   \       /   \               /   \       /   \
[1,2,3] [1,2] [1,3] [1]         [2,3]   [2]    [3]  []

        Here is a poorly drawn diagram but the idea is there. 
        We will start with an empty list (This will will represent our decision paths). 
        We can then iterate over all the numbers and from here make 2 decisions 
        (do we append this number to our list or not?). 
        We do this until we go through all the numbers in which we add the results of 
        this decision path to our result array. We do this for all paths.
        How we do this is to have our array that tracks the ongoing decision paths behave
        like a stack. Where we append the number at our current index, DFS recurse on this 
        path with the newly added element. THEN we can recurse on that path that will not
        have that decision.
        
        And because each decision is built off the previous, you need to have a global shared state (subset) to backtrack on decisions.
        '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, subset):
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            else:
                dfs(index + 1, subset + [nums[index]])
                
                dfs(index + 1, subset)
                
        res = []
                        
        dfs(0, [])
        return res
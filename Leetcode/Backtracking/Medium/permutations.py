'''
https://leetcode.com/problems/permutations/
'''
class Solution:
    '''
    Goal: We want to make every possible permutation of a given list of numbers
    
    Plan: 
    An approach we can take is to break this into sub problems. 
    
    What is a permutation? A permutation is the reordering of elements into different places. So lets look at the sample input: [1,2,3]. We know that the total number of permutations is 3!. This is because the number of choices we can make at each index to reorder each element is 3 * 2 * 1. 
    
    We can start with picking just 1 element. [3] then we can arrage all possibilities with [2] so we get [2,3] and [3,2] then we can arrage all possibilities with [1] so we get [1,2,3], [2,1,3], [2,3,1], [1,3,2], [3,1,2], [3,2,1].
    
    At every step of making permutations, we are adding an element and making all the different orderings.
    
    In our approach we are doing a DFS until there are no more elements in which we make an array with an empty list (base case). As we step back 1 layer, can add the first element to every possible position, which is just 1: [3], As we step back another layer, we now have access to [2,3] and will add the first element to every possible position: [2,3], [3,2]. Then we step back another layer and have access to [1,2,3] and can add the first element to all possible positions.
    
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) == 0):
            return [[]]
        
        # recurse until len(nums) == 0
        permutations = self.permute(nums[1:])
        
        res = []
        
        for p in permutations:
            for i in range(len(p) + 1):
                state = p.copy()
                state.insert(i, nums[0])
                res.append(state)
        return res
        
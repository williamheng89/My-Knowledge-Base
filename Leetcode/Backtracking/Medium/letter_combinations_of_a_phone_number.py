'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
class Solution:
    '''
    Goal: We will be given a string of numbers in the range of 2-9 and we will be finding all the possible letter combinations
    
    Plan:
    This is very similar to making permutations. Let's use the example '23'. 
    
    We know that the possible letters for '2' are [a,b,c] and the possible letters for '3' are [d,e,f]. So in the string '23', we will be making combinations that cover 2 spots, such that [a,b,c] + [d,e,f] which will be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
    
    So lets work out how our decision tree will look like:
    
    We will be starting with an empty string "" that we will be contributing to expand.
    
    We will set our base cast to stop the recursion when len(string) == len(digits)
    
    Then we simply iterate over the possibile letters of the current index, and recurse on the next index while concatenating the current letter to string we are building.
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        numbers_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        def backtrack(index, state):
            if (len(state) == len(digits)):
                res.append(state)
                return
            
            for letter in numbers_to_letters[digits[index]]:
                backtrack(index + 1, state + letter)
                
        if len(digits) >= 1:
            backtrack(0, "")
            
        return res
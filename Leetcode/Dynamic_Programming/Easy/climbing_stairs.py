'''
https://leetcode.com/problems/climbing-stairs/submissions/ 
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        memo = [0] * (n + 1)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        memo[3] = 3
        for i in range(4, n + 1):
            # Recurrence Relation
            memo[i] = memo[i-2] + memo[i-1] 
        return memo[n]
        
'''
Notes:

Let's solve for n=3.

For base cases:
step=1, we only have 1 way (1 step)
step=2, we have 2 ways (1 step, 1 step; 2 step)
step=3, we have 3 ways (1 step, 1 step, 1 step; 2 step, 1 step; 1 step, 2 step)

We need to recognize the recurrence relation and make sure we do not double count.

Originally, I thought the recurrence relation is memo[i] = memo[i-2] + 2 + memo[i-1] + 1

This is because I thought when we are at [i-1], there are 2 ways to get to i and when we are
at [i-1], there is only 1 way to get there. This is wrong because we are double counting.

The details are a little fuzzy, but what I thought out was that it is indeed:
memo[i] = memo[i-2] + 2 + memo[i-1] + 1 -3

There are indeed 3 ways to get from [i-2] and [i-1] to i. However, the 3 ways that it took to get them to [i-2]
and [i-1], respectively, must be eliminated because they are not valid paths to get to i (it is yet to be reached.)
This is established in the base cases where:

step=1, we only have 1 way (1 step)
step=2, we have 2 ways (1 step, 1 step; 2 step)
step=3, we have 3 ways (1 step, 1 step, 1 step; 2 step, 1 step; 1 step, 2 step)

Basically, from step=1, there are 2 was to get to step=3, from step=2, there is only 1 way to get to step=3.
BUT, the valid paths of steps=1 and steps=2 are invalid in respect for steps=3 because they haven't reached steps=3.
And thus the ways it took to get to step=1 is 1 and steps=2 is 2. 

And so we subtract 1 + 2 from the recurrence relation.
'''
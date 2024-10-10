'''
Dynamic Programming Basics
1. Top-Down Approach (Memoization)

Idea: Solve the problem recursively and store results of subproblems to avoid redundant calculations.
How it works:

Start solving the main problem.
Whenever a subproblem is encountered, check if it has already been solved. If yes, use the stored result. If not, solve it and store the result for future use
'''

# Example with Fibonacci:
def fib(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print(fib(10))  # Output: 55

# 2. Bottom-Up Approach (Tabulation)

# Idea: Solve the problem by solving all smaller subproblems first, and use their results to solve bigger problems.

# How it works:
# Start from the base case and iteratively solve up to the main problem by building the solution using a table.
# Code Example (Fibonacci - Bottom-Up):

def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fib(10))  # Output: 55

'''
Top-Down vs Bottom-Up

Top-Down (Memoization): Uses recursion and memoizes (caches) intermediate results.
Bottom-Up (Tabulation): Builds the solution iteratively from the smallest subproblems.
'''
# Introduction to Dynamic Programming
Dynamic Programming (DP) is a powerful algorithmic technique used to solve problems by breaking them down into smaller overlapping subproblems. It is particularly useful when a problem can be divided into similar subproblems whose results can be reused to avoid redundant work.

# Key Concepts of Dynamic Programming:
1. Optimal Substructure: A problem has an optimal substructure if an optimal solution to the problem can be constructed from optimal solutions to its subproblems.

2. Overlapping Subproblems: DP is effective when subproblems are solved multiple times. Instead of solving these subproblems again and again (as in recursive approaches), DP stores the results of subproblems to reuse later, reducing the time complexity.

3. Memoization vs. Tabulation:

    - Memoization (Top-Down Approach): Solving the problem recursively while storing the solutions to subproblems in a table (or dictionary) to avoid redundant computations.
    - Tabulation (Bottom-Up Approach): Iteratively solving all subproblems and storing their results in a table, starting with the smallest subproblems and working up to the original problem.

# How It’s Used:
Dynamic programming is commonly applied to optimization problems where we seek to maximize or minimize some value. It is used to:

- Break down a problem into simpler subproblems.
- Solve each subproblem once and store its result.
- Use the stored results to construct the solution to the original problem.

# Problems That Can Be Solved with Dynamic Programming:
Here are some common problem types that can be solved using DP:

- Fibonacci Sequence: A classic example where DP avoids recomputing Fibonacci numbers multiple times.
- Knapsack Problem: Deciding the most valuable combination of items to include in a knapsack without exceeding its weight limit.
- Longest Common Subsequence: Finding the longest subsequence that two sequences share.
- Matrix Chain Multiplication: Finding the optimal way to parenthesize a matrix multiplication sequence to minimize operations.
- Coin Change Problem: Finding the minimum number of coins needed to make a particular amount.

# How to Recognize DP Problems:
1. Repeated Subproblems: If you find yourself solving the same subproblem multiple times, consider using DP. For example, recursive solutions that recalculating the same values over and over may benefit from memoization.

2. Decision Making with Optimal Choices: If you need to make decisions at each step that depend on optimal solutions to subproblems, DP might be a good fit. For instance, choosing whether to include an item in a knapsack depends on previously calculated maximum values.

3. State-Dependent Solutions: If the solution can be described as depending on the results of one or more "states" that are combinations of previous decisions, DP can be used to cache the results of these states to avoid recomputation.
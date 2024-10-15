# Introduction to Greedy Algorithms
Greedy Algorithms are a problem-solving strategy used to find an optimal solution by making the best possible choice at each step. The idea is to pick the locally optimal choice with the hope that this leads to a globally optimal solution.

# Key Characteristics of Greedy Algorithms:
1. Greedy Choice Property: A global optimal solution can be arrived at by selecting the best local option at each stage.
2. Optimal Substructure: A problem exhibits optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems.

# How Greedy Algorithms Work:
- Greedy algorithms make decisions step-by-step, choosing the option that looks best in the current step.
- Once a decision is made, it is never reconsidered (non-revocable).

# Common Uses of Greedy Algorithms:
1. Optimization Problems: Problems that ask for the best solution under given constraints.
2. Scheduling: When tasks need to be performed with time constraints, like the Activity Selection Problem.
3. Graph Algorithms: Greedy algorithms are commonly used in graph-related problems such as finding the shortest path or minimum spanning tree. For example:
    - Dijkstra’s Algorithm: For finding the shortest path between nodes in a graph.
    - Prim’s or Kruskal’s Algorithm: For finding the Minimum Spanning Tree (MST).
4. Fractional Knapsack Problem: Where you aim to maximize profit by selecting items that can be fractionally divided.
5. Huffman Encoding: For data compression using variable-length codes.

## Example Problems:
- Coin Change Problem: Given coins of different denominations, find the minimum number of coins required to make a certain amount.
- Activity Selection Problem: Select the maximum number of activities that don't overlap in time.
- Job Sequencing Problem: Maximize profit by scheduling jobs within their deadlines.

# How to Recognize Greedy Problems:
1. Optimal Substructure: Check if the problem can be broken down into subproblems where the solution to each subproblem helps in solving the overall problem optimally.
2. Greedy Choice Property: If making the best local choice at every step leads to the best global solution, the problem might be suitable for a greedy algorithm.
3. No Backtracking: If the problem doesn’t require reconsidering previous choices (as opposed to techniques like backtracking), it may be a good candidate for a greedy approach.

# When Greedy Algorithms Fail:
- Greedy algorithms don’t always guarantee the optimal solution for every problem. For example, the 0/1 Knapsack Problem does not work with a greedy approach because the choice at each step might not lead to a globally optimal solution.
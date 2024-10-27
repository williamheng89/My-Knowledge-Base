# What is a Graph?
A graph is a collection of nodes (also called vertices) and edges connecting some pairs of these nodes. Graphs come in various forms:

- Directed Graphs (Digraphs): Edges have directions, so (A → B) is not the same as (B → A).
- Undirected Graphs: Edges have no direction, so (A — B) means A is connected to B and vice versa.
- Weighted Graphs: Edges have weights or costs, useful for scenarios where different connections have varying values, like distances or costs.
- Unweighted Graphs: All edges are equal in value or cost.

# How Graphs are Used
Graphs model relationships between entities in a variety of contexts:

- Social Networks: Nodes represent people; edges show friendships or connections.
- Maps and Routes: Nodes are locations, and edges represent possible routes. Weighted graphs often represent roads with distances or time.
- Network Routing: Graphs model internet infrastructure, with nodes as servers and edges as data paths.
- Dependencies: In project planning, graphs can represent tasks with dependencies, where one task needs to be completed before another can start.

# Problems Solved by Graphs
Graphs are highly versatile, solving problems across many domains. Key problems include:

1. Pathfinding: Finding the shortest or optimal path between nodes, like Dijkstra’s algorithm or A* for GPS routing.
2. Connected Components: Determining if a graph is fully connected or finding isolated sections, useful in network analysis.
3. Cycle Detection: Detecting cycles in directed graphs, often used in dependency and task scheduling to avoid circular dependencies.
4. Traversal: Visiting nodes in a specific order using Breadth-First Search (BFS) or Depth-First Search (DFS). Useful in solving puzzles, AI, and networking.
5. Matching: Finding pairings in bipartite graphs, such as matching applicants to jobs based on qualifications.
6. Network Flow: Maximizing flow in networks (e.g., pipes, data), useful in logistics and resource allocation.

# Recognizing Graph Problems
Graph-related problems typically involve relationships between pairs of items or the need to find optimal or connected structures. Signs of a graph problem:

- Connectivity: If you need to know if two items are connected or how many connected clusters exist.
- Pathfinding/Traversal: If you’re looking for routes or orders, such as the shortest path, or ways to reach a goal.
- Dependencies: If there’s a sequence with dependencies, such as a build order or project tasks with prerequisites.
- Pairing or Matching: When you need to find efficient pairings (e.g., applicants to positions).
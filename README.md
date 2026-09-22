# BFS vs A* – Grid-Based Robot Pathfinding

## SLE-2 | Introduction to Artificial Intelligence

**Student:** Mayuresh Patil  
**PRN:** 26UAM308  
**Division:** A  
**Course:** 02AML204

## Project Overview

This project compares the practical performance of **Breadth-First Search (BFS)** and **A* Search** for grid-based robot pathfinding.

The robot moves from a starting position `S` to a goal position `G` while avoiding obstacles `#`. Movement is allowed in four directions: up, down, left, and right.

## Algorithms

### BFS
- Uses a queue.
- Explores nodes level by level.
- Finds the shortest path for equal movement costs.
- Time Complexity: `O(V + E)`

### A*
- Uses a priority queue.
- Uses Manhattan Distance as the heuristic.
- Evaluation function: `f(n) = g(n) + h(n)`
- Heap-based implementation: `O(E log V)` worst-case bound.

## Performance Analysis

Three selected cases were tested using Python `timeit`.

| Case | Algorithm | Path Length | Nodes Expanded | Avg Time (ms) |
|------|-----------|-------------|----------------|---------------|
| Best | BFS | 1 | 3 | 0.0051 |
| Best | A* | 1 | 2 | 0.0066 |
| Average | BFS | 13 | 53 | 0.0799 |
| Average | A* | 13 | 32 | 0.0935 |
| Worst | BFS | 21 | 69 | 0.1044 |
| Worst | A* | 21 | 68 | 0.2009 |

## Profiling

Runtime profiling was performed using **py-spy**.

- `bfs_profile.svg` – BFS flame graph
- `astar_profile.svg` – A* flame graph

## Files

```text
bfs.py
AStar.py
case_analysis.py
bfs_profile.svg
astar_profile.svg
SLE_2_Profiling_Report_BFS_AStar_Submission.docx
README.md
AI_CONTRIBUTION_LOG.md

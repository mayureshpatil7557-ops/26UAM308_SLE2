from collections import deque
import heapq
import timeit

# ============================================================
# GRID
# ============================================================

grid = [
    "S...........",
    ".###.#####..",
    "...#.......#",
    ".#.#.#####.#",
    ".#.#.......#",
    ".#.#######.#",
    ".#.........#",
    ".#########.#",
    "...........#",
    "##########.#",
    "...........G"
]

ROWS = len(grid)
COLS = len(grid[0])

START = (0, 0)

# Three test cases
CASES = {
    "Best Case": (0, 1),
    "Average Case": (4, 9),
    "Worst Case": (10, 11)
}

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# ============================================================
# BFS
# ============================================================

def bfs(goal):
    queue = deque()
    queue.append((START, [START]))

    visited = set()
    visited.add(START)

    nodes_expanded = 0

    while queue:
        current, path = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        row, col = current

        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc

            if nr < 0 or nr >= ROWS:
                continue

            if nc < 0 or nc >= COLS:
                continue

            if grid[nr][nc] == '#':
                continue

            if (nr, nc) in visited:
                continue

            visited.add((nr, nc))
            queue.append(((nr, nc), path + [(nr, nc)]))

    return None, nodes_expanded


# ============================================================
# A*
# ============================================================

def astar(goal):

    def manhattan(pos):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    counter = 0

    open_list = []

    heapq.heappush(
        open_list,
        (manhattan(START), 0, counter, START, [START])
    )

    best_g = {START: 0}
    visited = set()

    nodes_expanded = 0

    while open_list:

        f, g, _, current, path = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == goal:
            return path, nodes_expanded

        row, col = current

        for dr, dc in DIRECTIONS:

            nr, nc = row + dr, col + dc

            if nr < 0 or nr >= ROWS:
                continue

            if nc < 0 or nc >= COLS:
                continue

            if grid[nr][nc] == '#':
                continue

            if (nr, nc) in visited:
                continue

            new_g = g + 1

            if (nr, nc) in best_g and best_g[(nr, nc)] <= new_g:
                continue

            best_g[(nr, nc)] = new_g

            counter += 1

            new_f = new_g + manhattan((nr, nc))

            heapq.heappush(
                open_list,
                (
                    new_f,
                    new_g,
                    counter,
                    (nr, nc),
                    path + [(nr, nc)]
                )
            )

    return None, nodes_expanded


# ============================================================
# RUN CASES
# ============================================================

RUNS = 10
REPS = 100

print("\n================================================")
print("     BFS AND A* CASE ANALYSIS")
print("================================================")

for case_name, goal in CASES.items():

    print("\n-------------------------------")
    print(case_name)
    print("-------------------------------")

    # ---------------- BFS ----------------

    bfs_path, bfs_nodes = bfs(goal)

    bfs_times = timeit.repeat(
        lambda: bfs(goal),
        repeat=RUNS,
        number=REPS
    )

    bfs_per_run = [(t / REPS) * 1000 for t in bfs_times]

    bfs_avg = sum(bfs_per_run) / len(bfs_per_run)

    # ---------------- A* ----------------

    astar_path, astar_nodes = astar(goal)

    astar_times = timeit.repeat(
        lambda: astar(goal),
        repeat=RUNS,
        number=REPS
    )

    astar_per_run = [(t / REPS) * 1000 for t in astar_times]

    astar_avg = sum(astar_per_run) / len(astar_per_run)

    # ---------------- Results ----------------

    print("\nBFS")
    print("Path Found     :", "Yes" if bfs_path else "No")
    print("Path Length    :", len(bfs_path) - 1 if bfs_path else "-")
    print("Nodes Expanded :", bfs_nodes)
    print("Average Time   : {:.4f} ms".format(bfs_avg))
    print("Minimum Time   : {:.4f} ms".format(min(bfs_per_run)))
    print("Maximum Time   : {:.4f} ms".format(max(bfs_per_run)))

    print("\nA*")
    print("Path Found     :", "Yes" if astar_path else "No")
    print("Path Length    :", len(astar_path) - 1 if astar_path else "-")
    print("Nodes Expanded :", astar_nodes)
    print("Average Time   : {:.4f} ms".format(astar_avg))
    print("Minimum Time   : {:.4f} ms".format(min(astar_per_run)))
    print("Maximum Time   : {:.4f} ms".format(max(astar_per_run)))

print("\n================================================")
print("             CASE ANALYSIS COMPLETE")
print("================================================")
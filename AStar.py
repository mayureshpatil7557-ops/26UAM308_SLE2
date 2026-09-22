import heapq
import timeit

# EXACTLY the same grid as bfs.py
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

start = None
goal = None
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'S':
            start = (r, c)
        elif grid[r][c] == 'G':
            goal = (r, c)

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def manhattan(pos):
    # |x1 - x2| + |y1 - y2|
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


def astar():
    counter = 0  # tie-breaker so heapq never compares tuples/lists
    open_list = []
    heapq.heappush(open_list, (manhattan(start), 0, counter, start, [start]))

    best_g = {start: 0}
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
            heapq.heappush(open_list,
                           (new_f, new_g, counter, (nr, nc), path + [(nr, nc)]))

    return None, nodes_expanded


# ---------- Run once for path / node count ----------
path, nodes = astar()

# ---------- Timing: 10 runs, each run = 100 repetitions ----------
RUNS = 10
REPS = 100
times = timeit.repeat(astar, repeat=RUNS, number=REPS)
per_run_ms = [(t / REPS) * 1000 for t in times]
avg_ms = sum(per_run_ms) / len(per_run_ms)

print("========== A* RESULTS ==========")
print("Heuristic       : Manhattan Distance")
print("Path Found      :", "Yes" if path else "No")
print("Path Length     :", len(path) - 1 if path else "-")
print("Nodes Expanded  :", nodes)
print("Runs            :", RUNS)
print("Avg Time (ms)   : {:.4f}".format(avg_ms))
print("Min Time (ms)   : {:.4f}".format(min(per_run_ms)))
print("Max Time (ms)   : {:.4f}".format(max(per_run_ms)))
# ---------- Profiling mode ----------
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "profile":
        for _ in range(100000):
            astar()
from collections import deque
import timeit

# S = Start, G = Goal, . = free, # = wall
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


def bfs():
    queue = deque()
    queue.append((start, [start]))

    visited = set()
    visited.add(start)

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


# ---------- Run once for path / node count ----------
path, nodes = bfs()

# ---------- Timing: 10 runs, each run = 100 repetitions ----------
RUNS = 10
REPS = 100
times = timeit.repeat(bfs, repeat=RUNS, number=REPS)
per_run_ms = [(t / REPS) * 1000 for t in times]
avg_ms = sum(per_run_ms) / len(per_run_ms)

print("========== BFS RESULTS ==========")
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
            bfs()
#############

def check(sr, sc, tr, tc):
    return sr == tr and sc == tc


def valid(grid, sr, sc):
    return sr > -1 and sr < len(grid) and sc > -1 and sc < len(grid[0]) and grid[sr][sc] == 1


def operation(grid, sr, sc, tr, tc, length, visited, queue):
    if check(sr, sc, tr, tc):
        return length
    elif valid(grid, sr, sc) and (sr, sc) not in visited:
        queue.insert(0, (sr, sc, length))
        visited.add((sr, sc))
    return -1


def shortestCellPath(grid, sr, sc, tr, tc):
    res = []
    length = 0
    queue = [(sr, sc, length)]
    visited = set()
    visited.add((sr, sc))
    while len(queue) > 0:
        nr, nc, l = queue.pop()
        min_path = operation(grid, nr + 1, nc, tr, tc, l + 1, visited, queue)
        if min_path > 0:
            return min_path
        min_path = operation(grid, nr, nc + 1, tr, tc, l + 1, visited, queue)
        if min_path > 0:
            return min_path
        min_path = operation(grid, nr - 1, nc, tr, tc, l + 1, visited, queue)
        if min_path > 0:
            return min_path
        min_path = operation(grid, nr, nc - 1, tr, tc, l + 1, visited, queue)
        if min_path > 0:
            return min_path

    return min_path

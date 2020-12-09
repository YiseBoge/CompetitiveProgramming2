import collections


class Solution:
    def hasValidPath(self, grid: list) -> bool:
        paths = [
            ((0, 1), (0, -1)),
            ((1, 0), (-1, 0)),
            ((1, 0), (0, -1)),
            ((1, 0), (0, 1)),
            ((-1, 0), (0, -1)),
            ((-1, 0), (0, 1))
        ]

        visited = set()
        start, target = (0, 0), (len(grid) - 1, len(grid[0]) - 1)
        queue = collections.deque([start])
        while queue:
            current = current_i, current_j = queue.popleft()
            if current == target:
                return True
            ind = grid[current_i][current_j] - 1
            for path_i, path_j in paths[ind]:
                rev = -path_i, -path_j
                new = new_i, new_j = current_i + path_i, current_j + path_j
                if (0 <= new_i < len(grid) and
                        0 <= new_j < len(grid[0]) and
                        new not in visited and
                        rev in paths[grid[new_i][new_j] - 1]):
                    visited.add(new)
                    queue.append(new)
        return False

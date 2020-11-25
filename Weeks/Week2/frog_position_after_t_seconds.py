import collections


class Solution:
    def frogPosition(self, n: int, edges: list, t: int, target: int) -> float:
        ways = []
        for i in range(n):
            ways.append([])
        for frm, to in edges:
            ways[frm - 1].append(to - 1)
            ways[to - 1].append(frm - 1)

        queue = collections.deque([(0, 0, 1)])
        visited = {0}
        while queue:
            current = queue.popleft()
            if current[1] > t:
                return 0

            total = 0
            for way in ways[current[0]]:
                if way not in visited:
                    total += 1
            if current[0] == target - 1:
                if current[1] == t or total == 0:
                    return current[2]
                return 0

            for way in ways[current[0]]:
                if way not in visited:
                    new = (way, current[1] + 1, current[2] / total)
                    queue.append(new)
                    visited.add(way)

        return 0

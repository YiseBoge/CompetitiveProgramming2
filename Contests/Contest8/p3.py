import collections
import sys


class Solution:
    def minimumJumps(self, forbidden: list, a: int, b: int, x: int) -> int:
        visited = set()
        for f in forbidden:
            visited.add((f, True))
            visited.add((f, False))

        start = (0, 0, False)
        queue = collections.deque([start])

        result = sys.maxsize
        while queue:
            current, jumps, back = queue.popleft()
            if current == x:
                result = min(result, jumps)

            new = current + a
            if new <= x + b and new and (new, True) not in visited:
                queue.append((new, jumps + 1, True))
                visited.add((new, True))

            new = current - b
            if back and new > 0 and new and (new, False) not in visited:
                queue.append((new, jumps + 1, False))
                visited.add((new, False))

        return -1 if result == sys.maxsize else result

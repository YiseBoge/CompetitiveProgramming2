import collections
import sys


class Solution:
    def shortestBridge(self, A: list) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        islands, index = [set(), set()], -1
        visited = set()

        def traverse(current):
            nonlocal A, islands, index, visited, directions
            islands[index].add(current)

            for d in directions:
                new_i, new_j = current[0] + d[0], current[1] + d[1]
                if (0 <= new_i < len(A) and
                        0 <= new_j < len(A[0]) and
                        (new_i, new_j) not in visited and
                        A[new_i][new_j] == 1):
                    visited.add((new_i, new_j))
                    traverse((new_i, new_j))

        for i in range(len(A)):
            for j in range(len(A[0])):
                if (i, j) not in visited and A[i][j] == 1:
                    index += 1
                    traverse((i, j))

        one, two = islands
        result = sys.maxsize
        for index in one:
            visited = set()
            queue = collections.deque([(index, 0)])
            while queue:
                current = queue.popleft()
                if current[1] >= result:
                    break
                for d in directions:
                    new_i, new_j = current[0][0] + d[0], current[0][1] + d[1]
                    if (0 <= new_i < len(A) and
                            0 <= new_j < len(A[0]) and
                            (new_i, new_j) not in one and
                            (new_i, new_j) not in visited):
                        if (new_i, new_j) in two:
                            result = min(result, current[1])
                            break
                        visited.add((new_i, new_j))
                        queue.append(((new_i, new_j), current[1] + 1))
        return result

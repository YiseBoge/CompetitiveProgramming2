import collections


class Solution:
    def openLock(self, deadends: list, target: str) -> int:
        start, visited = ("0000", 0), set(deadends)
        if start[0] in visited:
            return -1
        else:
            visited.add(start[0])

        queue = collections.deque([start])
        while queue:
            current = queue.popleft()
            if current[0] == target:
                return current[1]

            for i in range(4):
                num = int(current[0][i])
                possibles = (num + 1) % 9, (num - 1) % 10
                for digit in possibles:
                    new = current[0][:i] + str(digit) + current[0][i + 1:]
                    if new not in visited:
                        visited.add(new)
                        queue.append((new, current[1] + 1))

        return -1

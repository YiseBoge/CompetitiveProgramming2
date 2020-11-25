class Solution:
    def mostVisited(self, n: int, rounds: list) -> list:
        max_visits = 0
        visited = {i: 0 for i in range(n)}

        current = rounds[0] - 1
        i = 0
        while i < len(rounds):
            visited[current] += 1
            max_visits = max(max_visits, visited[current])
            if rounds[i] - 1 == current:
                i += 1
            current = (current + 1) % n

        result = []
        for i in visited:
            if visited[i] == max_visits:
                result.append(i + 1)
        return result

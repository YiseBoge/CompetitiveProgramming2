class Solution:
    def minTime(self, n: int, edges: list, hasApple: list) -> int:
        children = [[] for i in range(n)]
        for parent, child in edges:
            children[parent].append(child)
            children[child].append(parent)

        visited = set()

        def traverse(current):
            nonlocal children, hasApple, visited
            visited.add(current)
            result = 0
            for child in children[current]:
                if child not in visited:
                    res = traverse(child)
                    if res is not None:
                        result += (2 + res)

            if result == 0 and not hasApple[current]:
                return None
            return result

        min_dist = traverse(0)
        return min_dist if min_dist else 0

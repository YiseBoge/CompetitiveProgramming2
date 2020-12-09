class Solution:
    def catMouseGame(self, graph: list) -> int:
        visited = {(1, 2, 0)}
        memory = {}

        def traverse(mouse, cat, steps=0):
            nonlocal graph, visited, memory
            if steps >= 2 * len(graph):
                return 0
            state = (mouse, cat, steps)
            if state in memory:
                return memory[state]
            if mouse == 0:
                return 1
            if cat == mouse:
                return 2

            ind = steps % 2
            options = [mouse, cat]
            current = options[ind]
            results, result = set(), 0
            for n in graph[current]:
                new = [mouse, cat, steps + 1]
                new[ind] = n
                new = tuple(new)
                new_visit = (new[0], new[1], 1 - ind)
                if new_visit in visited:
                    results.add(0)
                if new_visit not in visited and new[1] != 0:
                    visited.add(new_visit)
                    r = traverse(new[0], new[1], new[2])
                    visited.remove(new_visit)
                    results.add(r)
                    if r == ind + 1:
                        break
            result = ind + 1 if ind + 1 in results else min(results)
            memory[state] = result
            return result

        return traverse(1, 2, 0)

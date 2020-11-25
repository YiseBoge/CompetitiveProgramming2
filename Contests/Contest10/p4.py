class Solution:
    def minimumEffort(self, tasks: list) -> int:
        sorted_tasks = sorted(tasks, key=lambda x: x[1] - x[0], reverse=True)
        added = 0
        remaining = 0
        for actual, initial in sorted_tasks:
            if remaining < initial:
                added += initial - remaining
                remaining = initial
            remaining -= actual
        return added

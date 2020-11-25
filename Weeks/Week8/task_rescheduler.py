import collections


class Solution:
    def leastInterval(self, tasks: list, n: int) -> int:
        tasks_count = {}
        intervals = 0
        queue = collections.deque()
        end_after = len(tasks)

        for i in tasks:
            if tasks_count.get(i):
                tasks_count[i] += 1
            else:
                tasks_count[i] = 1

        while end_after > 0:
            if len(queue) > n:
                queue.popleft()

            item = None
            max_count = 0
            q = set(queue)
            for k in tasks_count:
                if k not in q and tasks_count[k] > max_count:
                    max_count = tasks_count[k]
                    item = k

            if item:
                tasks_count[item] -= 1
                end_after -= 1
            queue.append(item)
            intervals += 1

        return intervals

import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        heap = []
        for c in counts:
            item = (-counts[c], c)
            heapq.heappush(heap, item)

        result = []
        while heap:
            item = heapq.heappop(heap)
            result.append(item[1] * -item[0])

        return "".join(result)

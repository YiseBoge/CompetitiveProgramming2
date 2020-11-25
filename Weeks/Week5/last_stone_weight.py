import heapq


class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x < y:
                heapq.heappush(heap, x - y)

        return 0 if not heap else -heap[0]

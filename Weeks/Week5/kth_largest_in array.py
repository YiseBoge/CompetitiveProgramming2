import heapq


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) >= k and heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
            if len(heap) < k:
                heapq.heappush(heap, num)

        return heap[0]

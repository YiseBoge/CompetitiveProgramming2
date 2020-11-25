import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list) -> int:
        heap = [1] + [x for x in primes]
        visited = set(heap)
        count = 1

        while count < n:
            current = heapq.heappop(heap)
            count += 1
            for p in primes:
                product = current * p
                if product not in visited:
                    visited.add(product)
                    heapq.heappush(heap, product)
        return heapq.heappop(heap)

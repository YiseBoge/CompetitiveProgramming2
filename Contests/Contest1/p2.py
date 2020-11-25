import collections


class Solution:
    def maxCoins(self, piles: list) -> int:
        sorted_piles = sorted(piles)
        items = collections.deque(sorted_piles)
        result = 0
        while items:
            items.pop()
            items.popleft()
            result += items.pop()

        return result

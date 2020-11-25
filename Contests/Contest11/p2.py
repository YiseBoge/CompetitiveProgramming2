class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1

        odds = 0
        for el in counts:
            if el % 2 == 1:
                odds += 1
        return len(s) >= k >= odds

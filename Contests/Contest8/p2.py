import sys


class Solution:
    def minimumDeletions(self, s: str) -> int:
        result = sys.maxsize
        total_a = 0
        for el in s:
            if el == 'a':
                total_a += 1

        a_count = b_count = 0
        for el in s:
            if el == 'a':
                a_count += 1
            elif el == 'b':
                remaining = total_a - a_count
                result = min(result, remaining + b_count)
                b_count += 1

        result = min(result, b_count)
        return result

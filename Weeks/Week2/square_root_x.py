class Solution:
    def mySqrt(self, x: int) -> int:
        result = x
        start, end = 0, x
        while start <= end:
            mid = (start + end) // 2
            val = mid * mid
            if val <= x:
                result = mid
                start = mid + 1
            elif val > x:
                end = mid - 1
        return result

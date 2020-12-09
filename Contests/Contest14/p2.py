import math


class Solution:
    def sumFourDivisors(self, nums: list) -> int:
        result = 0
        for num in nums:
            divisors, count = 0, 0
            for i in range(1, math.floor(math.sqrt(num)) + 1):
                if num % i == 0:
                    res = num // i
                    divisors += res + i
                    count += 1 if res == i else 2
            if count == 4:
                result += divisors
        return result

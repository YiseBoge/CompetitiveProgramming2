class Solution:
    def maxSatisfaction(self, satisfaction: list) -> int:
        satisfaction.sort()
        result = 0
        for i, s in enumerate(satisfaction):
            result += (i + 1) * s

        total_sum = sum(satisfaction)
        for i, val in enumerate(satisfaction):
            res = total_sum
            if res >= 0:
                break
            result = result - res
            total_sum -= satisfaction[i]

        return result

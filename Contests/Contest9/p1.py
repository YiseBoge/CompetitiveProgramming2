class Solution:
    def trimMean(self, arr: list) -> float:
        sorted_arr = sorted(arr)
        limit = len(arr) // 20
        total = count = 0
        for i in range(limit, len(arr) - limit):
            total += sorted_arr[i]
            count += 1
        return total / count

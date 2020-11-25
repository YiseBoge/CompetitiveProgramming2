class Solution:
    def isPossible(self, nums: list) -> bool:
        results = []
        for num in nums:
            for j in range(len(results) - 1, -1, -1):
                if results[j][0] == num - 1:
                    results[j] = (num, results[j][1] + 1)
                    break
            else:
                results.append((num, 1))

        for res in results:
            if res[1] < 3:
                return False
        return True

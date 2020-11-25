class Solution:
    def minOperations(self, nums: list, x: int) -> int:
        sum_1, sum_2 = [], []
        cur_1, cur_2 = 0, 0

        best_steps = 100001
        for ind_1 in range(len(nums)):
            ind_2 = (len(nums) - 1) - ind_1
            cur_1 += nums[ind_1]
            cur_2 += nums[ind_2]

            if cur_1 <= x:
                sum_1.append(cur_1)
                if cur_1 == x:
                    best_steps = min(best_steps, len(sum_1))

            if cur_2 <= x:
                sum_2.append(cur_2)
                if cur_2 == x:
                    best_steps = min(best_steps, len(sum_2))

        for i in range(len(sum_1)):
            max_length = (len(nums) - 1) - i
            start, end, target = 0, min(len(sum_2), max_length) - 1, x - sum_1[i]
            while start <= end:
                mid = (start + end) // 2
                val = sum_2[mid]

                if val == target:
                    steps = i + mid + 2
                    best_steps = min(best_steps, steps)
                    break
                elif val < target:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1 if best_steps == 100001 else best_steps

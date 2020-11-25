class Solution:
    def jump(self, nums: list) -> int:
        result = 0
        if len(nums) == 1:
            return 0

        i = 0
        while i < len(nums):
            current = nums[i]
            max_found = 0, None
            for j in range(current):
                new = i + j + 1
                if new == len(nums) - 1:
                    return result + 1

                if nums[new] + j >= max_found[0]:
                    max_found = nums[new] + j, new
            i = max_found[1]
            result += 1

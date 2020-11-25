class Solution:
    def specialArray(self, nums: list) -> int:
        sorted_nums = sorted(nums, reverse=True)

        for i, val in enumerate(sorted_nums):
            if i + 1 > val:
                return -1 if val == i else i

        return len(sorted_nums)

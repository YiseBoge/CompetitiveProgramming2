class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        result = len(nums)
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            val = nums[mid]
            if val >= target:
                result = mid
                end = mid - 1
            elif val < target:
                start = mid + 1
        return result

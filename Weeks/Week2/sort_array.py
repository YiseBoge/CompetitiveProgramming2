class Solution:
    def sortArray(self, nums: list) -> list:

        def merge(first, second):
            result = []
            left = right = 0
            while left < len(first) or right < len(second):
                if left < len(first) and (right >= len(second) or first[left] <= second[right]):
                    result.append(first[left])
                    left += 1
                elif right < len(second) and (left >= len(first) or second[right] < first[left]):
                    result.append(second[right])
                    right += 1
            return result

        def sort(start, end):
            mid = (start + end) // 2
            if end - start < 0:
                return []
            elif end - start == 0:
                return [nums[start]]
            return merge(sort(start, mid), sort(mid + 1, end))

        return sort(0, len(nums) - 1)

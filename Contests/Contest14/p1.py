class Solution:
    def createTargetArray(self, nums: list, index: list) -> list:
        result = []
        for i, val in zip(index, nums):
            result.insert(i, val)
        return result

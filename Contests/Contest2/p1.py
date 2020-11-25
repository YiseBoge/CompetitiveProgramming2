class Solution:
    def busyStudent(self, startTime: list, endTime: list, queryTime: int) -> int:
        result = 0
        for i, j in zip(startTime, endTime):
            if i <= queryTime <= j:
                result += 1
        return result

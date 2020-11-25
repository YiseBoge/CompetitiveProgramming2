class Solution:
    def merge(self, intervals: list) -> list:
        sorted_intervals, results = sorted(intervals), []

        for interval in sorted_intervals:
            if results and interval[0] <= results[-1][1]:
                results[-1][1] = max(interval[1], results[-1][1])
            else:
                results.append(interval)
        return results

class Solution:
    def reconstructQueue(self, people: list) -> list:
        sorted_heights = sorted(people)
        result = [None] * len(sorted_heights)
        for height, front in sorted_heights:
            count = 0
            for i in range(len(result)):
                if count == front and result[i] is None:
                    result[i] = height, front
                    break
                elif result[i] is None or result[i][0] == height:
                    count += 1
        return result

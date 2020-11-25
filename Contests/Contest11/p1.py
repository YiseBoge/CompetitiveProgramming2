class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(num):
            result = 0
            for digit in str(num):
                result += int(digit)
            return result

        store = [0] * 37
        for i in range(n):
            store[digit_sum(i + 1)] += 1

        result, needed = 0, max(store)
        for el in store:
            if el == needed:
                result += 1

        return result

class Solution:
    def waysToMakeFair(self, nums: list) -> int:
        even_sum = odd_sum = 0
        even_array, odd_array = [], []

        for i, num in enumerate(nums):
            even_array.append(even_sum)
            odd_array.append(odd_sum)
            if i % 2 == 0:
                even_sum += num
            else:
                odd_sum += num

        result = 0
        for i, num in enumerate(nums):
            left_evens, left_odds = even_array[i], odd_array[i]
            remaining_evens, remaining_odds = even_sum - left_evens, odd_sum - left_odds
            if i % 2 == 0:
                remaining_evens -= num
            else:
                remaining_odds -= num

            if left_evens + remaining_odds == left_odds + remaining_evens:
                result += 1
        return result

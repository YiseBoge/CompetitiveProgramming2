class Solution:
    def isPossibleDivide(self, nums: list, k: int) -> bool:
        count_array = {}
        for num in nums:
            if num in count_array:
                count_array[num] += 1
            else:
                count_array[num] = 1

        while count_array.keys():
            start = min(count_array.keys())
            for i in range(k):
                num = start + i
                if num in count_array:
                    count_array[num] -= 1
                    if count_array[num] == 0:
                        count_array.pop(num)
                else:
                    return False
        return True

class Solution:
    def decrypt(self, code: list, k: int) -> list:
        full_list = code * 3
        sum_array, total = [], 0
        for item in full_list:
            total += item
            sum_array.append(total)

        result = [0] * len(code)
        start = len(code)
        for i in range(len(code)):
            ind = start + i

            if (code[i] > 0 and k > 0) or (code[i] < 0 and k < 0):
                res = sum_array[ind + abs(k)] - sum_array[ind]
                result[i] = res
            elif (code[i] < 0 and k > 0) or (code[i] > 0 and k < 0):
                res = sum_array[ind - 1] - sum_array[ind - abs(k) - 1]
                result[i] = res

        return result

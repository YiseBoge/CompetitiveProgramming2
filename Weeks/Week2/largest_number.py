class Solution:
    def largestNumber(self, nums: list) -> str:
        def greater_or_equal(n1, n2, ind1=0, ind2=0):
            while ind1 < len(n1) or ind2 < len(n2):
                if ind1 == len(n1):
                    return greater_or_equal(n1, n2, 0, ind2)
                elif ind2 == len(n2):
                    return greater_or_equal(n1, n2, ind1, 0)
                elif n1[ind1] != n2[ind2]:
                    return n1[ind1] >= n2[ind2]
                ind1 += 1
                ind2 += 1
            return True

        def merge(first, second):
            res = []
            left = right = 0
            while left < len(first) or right < len(second):
                if left < len(first) and (right >= len(second) or greater_or_equal(first[left], second[right])):
                    res.append(str(first[left]))
                    left += 1
                elif right < len(second) and (left >= len(first) or greater_or_equal(second[right], first[left])):
                    res.append(str(second[right]))
                    right += 1
            return res

        def sort(start, end):
            mid = (start + end) // 2
            if end - start < 0:
                return []
            elif end - start == 0:
                return [str(nums[start])]
            return merge(sort(start, mid), sort(mid + 1, end))

        result = "".join(sort(0, len(nums) - 1))
        if result != "" and result[0] == "0":
            return "0"
        return result

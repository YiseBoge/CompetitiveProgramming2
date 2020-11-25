class Solution:
    def findLatestStep(self, arr: list, m: int) -> int:
        if m == len(arr):
            return m
        ends, starts = {}, {}
        last_found = -1

        for ind, val in enumerate(arr):
            left = val - 1 if val - 1 in ends else None
            right = val + 1 if val + 1 in starts else None

            if left and right:
                length1, length2 = left - ends[left], starts[right] - right
                if length1 == m - 1 or length2 == m - 1:
                    last_found = ind
                l, r = ends[left], starts[right]
                starts[l], ends[r] = r, l
                del ends[left]
                del starts[right]
            elif left:
                length = left - ends[left]
                if length == m - 1:
                    last_found = ind
                ends[val] = ends[left]
                starts[ends[left]] = val
                del ends[left]
            elif right:
                length = starts[right] - right
                if length == m - 1:
                    last_found = ind
                starts[val] = starts[right]
                ends[starts[right]] = val
                del starts[right]
            else:
                starts[val] = val
                ends[val] = val
        return last_found

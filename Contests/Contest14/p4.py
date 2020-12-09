class Solution:
    def longestPrefix(self, s: str) -> str:
        result = -1
        for prefix_end in range(len(s) - 1):
            new_start = len(s) - prefix_end - 1
            if s[0] == s[new_start] and s[:prefix_end + 1] == s[new_start:]:
                result = max(result, prefix_end)
        return s[:result + 1]

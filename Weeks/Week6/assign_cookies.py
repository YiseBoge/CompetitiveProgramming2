class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        children = sorted(g)
        cookies = sorted(s)

        i = j = result = 0
        while i < len(children) and j < len(cookies):
            if cookies[j] >= children[i]:
                result += 1
                i += 1
                j += 1
            else:
                j += 1
        return result

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        start = len(b) // len(a)
        string = a * start

        for i in range(3):
            if b in string:
                return start + i
            string = string + a

        return -1

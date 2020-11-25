class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack, popped = [], 0
        for n in num:
            current = int(n)
            while stack and int(stack[-1]) > current and popped < k:
                stack.pop()
                popped += 1
            if not stack and current == 0:
                continue
            stack.append(str(current))

        while stack and popped < k:
            stack.pop()
            popped += 1

        return "".join(stack) if stack else "0"

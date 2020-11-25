class FreqStack:

    def __init__(self):
        self.stack = []
        self.frequencies = {}

    def push(self, x: int) -> None:
        if x not in self.frequencies:
            self.frequencies[x] = 1
        else:
            self.frequencies[x] += 1

        if not self.stack:
            self.stack.append([x, 1, 1])
        else:
            max_freq = self.stack[-1][2]
            self.stack.append([x, self.frequencies[x], max(max_freq, self.frequencies[x])])

    def pop(self) -> int:
        temp = []
        while self.stack[-1][1] < self.stack[-1][2]:
            temp.append(self.stack.pop())

        result = self.stack.pop()[0]

        for el in reversed(temp):
            freq = 1 if not self.stack else max(self.stack[-1][2], el[1])
            el[2] = freq
            self.stack.append(el)

        self.frequencies[result] -= 1
        return result

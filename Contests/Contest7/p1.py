class OrderedStream:

    def __init__(self, n: int):
        self.store = [None] * n
        self.ptr = 0

    def insert(self, id: int, value: str) -> list:
        ind = id - 1
        self.store[ind] = value

        result, i = [], self.ptr
        while i < len(self.store) and self.store[i]:
            result.append(self.store[i])
            self.ptr = i + 1
            i += 1
        return result

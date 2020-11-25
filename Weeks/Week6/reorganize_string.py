class Solution:
    def reorganizeString(self, S: str) -> str:
        collected_chars = {}
        result = ""
        length = len(S)

        for i in S:
            if collected_chars.get(i) is None:
                collected_chars[i] = 1
            else:
                collected_chars[i] += 1

        m = None
        for k in range(length):
            m = self.__max(collected_chars, m)
            if m == '':
                return ''
            result += m
            collected_chars[m] -= 1

        return result

    def __max(self, L, ex):
        m = ""
        for i in L.keys():
            if i is not ex and L[i] > 0:
                if L.get(m) is None or (i is not ex and L[i] > 0 and L[i] > L[m]):
                    m = i

        return m

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count_1 = {}
        for w in word1:
            if w in count_1:
                count_1[w] += 1
            else:
                count_1[w] = 1

        count_2 = {}
        for w in word2:
            if w in count_2:
                count_2[w] += 1
            else:
                count_2[w] = 1

        k1, v1 = sorted(count_1.keys()), sorted(count_1.values())
        k2, v2 = sorted(count_2.keys()), sorted(count_2.values())
        return k1 == k2 and v1 == v2

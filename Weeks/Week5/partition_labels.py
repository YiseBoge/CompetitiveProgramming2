class Solution:
    def partitionLabels(self, S: str) -> list:
        results = []
        start, end = 0, 0
        for i, el in enumerate(S):
            for j in range(end, len(S)):
                if S[j] == S[i]:
                    end = j
            if i == end:
                results.append(end - start + 1)
                start, end = i + 1, i + 1

        return results

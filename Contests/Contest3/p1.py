class Solution:
    def stringMatching(self, words: list) -> list:
        results = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    results.append(words[i])
                    break
        return results

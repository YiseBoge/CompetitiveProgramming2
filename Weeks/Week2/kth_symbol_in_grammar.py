class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def generate(remaining, index, flipped=False):
            if remaining <= 1:
                return 1 if flipped else 0
            remaining = remaining // 2
            flipped = flipped if index < remaining else not flipped
            index = index % remaining
            return generate(remaining, index, flipped)

        result = generate(2 ** (N - 1), K - 1)
        return result

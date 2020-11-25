class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counts = {str(i): 0 for i in range(10)}
        for digit in secret:
            counts[digit] += 1

        visited = set()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                counts[secret[i]] -= 1
                visited.add(i)

        cows = 0
        for i, digit in enumerate(guess):
            if i not in visited and counts[digit] > 0:
                counts[digit] -= 1
                cows += 1

        return f"{len(visited)}A{cows}B"

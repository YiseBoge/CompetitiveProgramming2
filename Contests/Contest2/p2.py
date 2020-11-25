class Solution:
    def arrangeWords(self, text: str) -> str:
        words = {}
        split_text = text.split(" ")
        split_text[0] = split_text[0].lower()
        for word in split_text:
            length = len(word)
            if length in words:
                words[length].append(word)
            else:
                words[length] = [word]

        result = []
        for length in sorted(words.keys()):
            result += words[length]
        result[0] = result[0].capitalize()
        return " ".join(result)

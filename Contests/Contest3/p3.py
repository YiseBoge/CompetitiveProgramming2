class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": "\"",
            "&apos;": "\'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
        }
        result = []
        i = 0
        while i < len(text):
            if text[i] == "&":
                key = []
                while i < len(text):
                    key.append(text[i])
                    if text[i] == ";":
                        break
                    i += 1
                k = "".join(key)
                if k in entities:
                    result.append(entities[k])
                else:
                    result.append(k)
            else:
                result.append(text[i])
            i += 1
        return "".join(result)

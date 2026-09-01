class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0

        while i < len(words):
            line = []
            length = 0

            while i < len(words) and length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1

            spaces = maxWidth - length
            gaps = len(line) - 1

            if i == len(words) or gaps == 0:
                res.append(" ".join(line) + " " * (maxWidth - length - gaps))
                continue

            extra = spaces // gaps
            remainder = spaces % gaps

            text = ""

            for j in range(gaps):
                text += line[j]
                text += " " * (extra + (1 if j < remainder else 0))

            text += line[-1]
            res.append(text)

        return res 
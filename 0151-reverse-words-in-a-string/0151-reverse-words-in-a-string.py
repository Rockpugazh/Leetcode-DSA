class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""

        for ch in s:
            if ch != " ":
                word += ch
            else:
                if word != "":
                    words.append(word)
                    word = ""

        if word != "":
            words.append(word)

        left = 0
        right = len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]

            left += 1
            right -= 1

        result = ""

        for word in words:
            if result != "":
                result += " "
            result += word

        return result
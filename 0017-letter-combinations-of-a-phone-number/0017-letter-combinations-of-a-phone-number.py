class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = [""]

        for digit in digits:
            temp = []

            for word in result:
                for letter in phone[digit]:
                    temp.append(word + letter)

            result = temp

        return result
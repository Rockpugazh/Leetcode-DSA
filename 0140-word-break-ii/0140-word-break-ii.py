class Solution:

    def wordBreak(self, s, wordDict):

        wordSet = set(wordDict)

        def backtrack(start):

            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, len(s) + 1):

                word = s[start:end]

                if word in wordSet:

                    remaining = backtrack(end)

                    for sentence in remaining:

                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)

            return result

        return backtrack(0)
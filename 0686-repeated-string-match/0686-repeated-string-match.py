class Solution:
    def repeatedStringMatch(self, a, b):
        count = 1
        s = a

        while len(s) < len(b):
            s += a
            count += 1

        if b in s:
            return count

        s += a

        if b in s:
            return count + 1

        return -1
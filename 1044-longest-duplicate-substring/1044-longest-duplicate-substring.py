class Solution:
    def longestDupSubstring(self, s):
        n = len(s)

        base = 26
        mod1 = 1000000007
        mod2 = 1000000009

        def check(length):
            if length == 0:
                return 0

            h1 = 0
            h2 = 0

            power1 = pow(base, length - 1, mod1)
            power2 = pow(base, length - 1, mod2)

            for i in range(length):
                value = ord(s[i]) - ord('a') + 1
                h1 = (h1 * base + value) % mod1
                h2 = (h2 * base + value) % mod2

            seen = {(h1, h2): 0}

            for i in range(length, n):
                old = ord(s[i - length]) - ord('a') + 1
                new = ord(s[i]) - ord('a') + 1

                h1 = (h1 - old * power1) % mod1
                h1 = (h1 * base + new) % mod1

                h2 = (h2 - old * power2) % mod2
                h2 = (h2 * base + new) % mod2

                key = (h1, h2)

                if key in seen:
                    return seen[key]

                seen[key] = i - length + 1

            return -1

        left = 1
        right = n - 1

        best_start = -1
        best_length = 0

        while left <= right:
            mid = (left + right) // 2

            start = check(mid)

            if start != -1:
                best_start = start
                best_length = mid
                left = mid + 1
            else:
                right = mid - 1

        if best_start == -1:
            return ""

        return s[best_start:best_start + best_length]
        
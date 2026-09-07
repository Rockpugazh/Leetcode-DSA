class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # Step 1: Replace useless numbers
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        # Step 2: Mark numbers that exist
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        # Step 3: Find the first unmarked position
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        # Everything from 1 to n exists
        return n + 1
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = 0
        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        n = len(nums)
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break
        return [duplicate, missing]
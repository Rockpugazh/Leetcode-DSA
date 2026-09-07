class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()

        n = len(nums)
        result = [0] * n

        left = (n + 1) // 2 - 1
        right = n - 1

        for i in range(n):
            if i % 2 == 0:
                result[i] = nums[left]
                left -= 1
            else:
                result[i] = nums[right]
                right -= 1

        nums[:] = result
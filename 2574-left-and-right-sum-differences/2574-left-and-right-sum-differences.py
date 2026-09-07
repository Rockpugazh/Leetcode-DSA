class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []

        for i in range(n):
            leftSum = sum(nums[:i])
            rightSum = sum(nums[i+1:])
            
            answer.append(abs(leftSum - rightSum))

        return answer
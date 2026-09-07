class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            i= abs(num)-1
            nums[i]=-abs(nums[i])
        result=[]
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(i+1)
        return result
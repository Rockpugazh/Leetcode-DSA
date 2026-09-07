class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest=min(nums)
        Largest=max(nums)
        while smallest != 0:
            Largest,smallest = smallest, Largest % smallest
        return Largest
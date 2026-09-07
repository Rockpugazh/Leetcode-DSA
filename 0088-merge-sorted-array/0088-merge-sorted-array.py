class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k=0
        for i in range(m):
            if nums1[i] in nums1:
                nums1[k]=nums1[i]
                k+=1
        for j in range(n):
            if nums2[j] in nums2:
                nums1[k]=nums2[j]
                k+=1
        return nums1.sort()
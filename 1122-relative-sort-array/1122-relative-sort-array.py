class Solution:
    def relativeSortArray(self, arr1, arr2):
        result = []

        for num in arr2:
            while num in arr1:
                result.append(num)
                arr1.remove(num)

        arr1.sort()
        result.extend(arr1)

        return result
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:        
        result = []
        n = len(arr)        
        for size in range(n, 1, -1):                   
            max_index = arr.index(size)                       
            if max_index != size - 1:                                
                if max_index != 0:
                    arr[:max_index + 1] = arr[:max_index + 1][::-1]
                    result.append(max_index + 1)                                
                arr[:size] = arr[:size][::-1]
                result.append(size)        
        return result
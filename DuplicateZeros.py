class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i= 0
        while i < len(arr)-1:
            if arr[i] ==0:
                arr.insert (i+1,0)
                del arr[(len(arr)-1)]
                i = i+2
            else:
                i = i+1
                
                
                
#Example 1:

#Input: arr = [1,0,2,3,0,4,5,0]
#Output: [1,0,0,2,3,0,0,4]
#Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

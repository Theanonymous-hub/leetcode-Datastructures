#Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

#After doing so, return the array.


#Constraints:

#1 <= arr.length <= 104
#1 <= arr[i] <= 105

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMaximum = -1
         
        for i in range(len(arr) -1,-1, -1):
            newMaximum = max(rightMaximum, arr[i])
            arr[i] =rightMaximum
            rightMaximum = newMaximum
        return arr

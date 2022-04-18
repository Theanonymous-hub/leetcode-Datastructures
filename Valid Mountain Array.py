#Given an array of integers arr, return true if and only if it is a valid mountain array.

#Recall that arr is a mountain array if and only if:

#arr.length >= 3
#There exists some i with 0 < i < arr.length - 1 such that:
#arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

#Constraints:

#1 <= arr.length <= 104
#0 <= arr[i] <= 104

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        strictlyInclined = False
        strictlyDeclined = False
        
        for i in range (len (arr)-1):
            if (arr[i+1] < arr[i]):
                if(strictlyInclined == False):
                    return False
                strictlyDeclined = True
            elif (arr[i+1] > arr[i]):
                if (strictlyDeclined == True):
                    return False
                strictlyInclined = True
            else:
                return False
        if strictlyInclined and strictlyDeclined:
            return True
        else:
            return False
        

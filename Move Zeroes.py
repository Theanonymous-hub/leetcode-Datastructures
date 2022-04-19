#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

#Constraints:

#1 <= nums.length <= 104
#-231 <= nums[i] <= 231 - 1
 
  
  class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        nxt_non_zero = 0
        for n in nums:
            if n!=0:
                nums[nxt_non_zero]=n
                nxt_non_zero +=1
        for zero in range (1,zero_count +1):
            nums[-zero] = 0

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_pointer = 1
        
        for right_pointer in range (1,len (nums)):
            #comparing whether right pointer is new or existing
            if nums[right_pointer] != nums[right_pointer-1]:
                nums[left_pointer] = nums[right_pointer]
                left_pointer +=1
        return left_pointer

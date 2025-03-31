class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        j = 2  # Pointer to track the position for the next valid element
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:  # Ensure at most two occurrences
                nums[j] = nums[i]
                j += 1
        
        return j
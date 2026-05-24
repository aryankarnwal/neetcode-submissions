class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = ''
        
        for i in range(len(nums)):
            if nums[i] == last:
                nums[i] = -999
            if nums[i] != -999:
                last = nums[i]
        
        while -999 in nums:
            nums.remove(-999)
        return len(nums)

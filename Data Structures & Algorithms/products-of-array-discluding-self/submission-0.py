class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums) 
        suffix = [0] * len(nums) 
        res = [0] * len(nums)

        prev = 1
        for i in range(len(nums)):
            
            prefix[i] = prev
            prev *= nums[i]

        prev = 1

        for i in range(len(nums)-1, -1, -1):
            
            suffix[i] = prev
            prev *= nums[i]
        
        for i in range(len(prefix)):
            res[i] = prefix[i] * suffix[i]
        return res

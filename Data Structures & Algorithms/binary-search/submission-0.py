class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        
        while l <= r:
            m = (l+r)//2
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[m] == target:
                return m
            else:
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
            
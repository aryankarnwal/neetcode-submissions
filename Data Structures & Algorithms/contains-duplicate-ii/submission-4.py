class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = k 

        if k >= len(nums):
            return len(nums) != len(set(nums))
        while r != len(nums):
            window = nums[l:r+1]
            seen = set(window)
            if len(seen) != len(window):
                return True
            l += 1
            r += 1
        return False
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        if target == nums[0]:
            return 0
        while l<=r:
            if target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            
            if target > nums[l]:
                l+=1
            
            if target < nums[r]:
                r -= 1
            
        
        return -1
        
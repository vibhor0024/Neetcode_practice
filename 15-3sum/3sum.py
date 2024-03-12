class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        nums.sort()

        for i,n in enumerate(nums):
            if i>0 and nums[i-1] == n:
                continue
            
            l=i+1
            r = len(nums) - 1
            while l<r:
                csum = n + nums[l] + nums[r]
                if csum > 0:
                    r -= 1
                elif csum < 0:
                    l += 1
                else:
                    res.append([nums[l],nums[r],n])
                    r -= 1
                    while r>l and nums[r] == nums[r+1]:
                        r -= 1
        
        return res
                



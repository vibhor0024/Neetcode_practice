class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict1 = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in dict1:
                return [dict1[diff],i]
            dict1[n] = i
        
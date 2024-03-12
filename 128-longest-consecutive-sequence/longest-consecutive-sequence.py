class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in set1:
                length = 0
                while (num + length) in set1:
                    length += 1
                longest = max(length,longest)
        
        return longest



        
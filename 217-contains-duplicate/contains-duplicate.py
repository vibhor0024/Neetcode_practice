class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = set()

        for num in nums:
            if num in set1:
                return True
            
            set1.add(num)
        
        return False


            

            
            
        
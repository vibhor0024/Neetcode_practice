class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1

        while l<r:
            csum = numbers[l] + numbers[r]
            if csum > target:
                r -= 1
            
            elif csum < target:
                l += 1
            
            else:
                return [l+1,r+1]
                
        
        return []
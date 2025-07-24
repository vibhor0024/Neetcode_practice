class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = 0
        r = 0
        d = collections.deque()
        res = []
        for r in range(len(nums)):
            while d and nums[d[-1]] <= nums[r]:
                d.pop()
            
            d.append(r)

            if l > d[0]:
                d.popleft()
            
            if r+1 >= k:
                res.append(nums[d[0]])
                l += 1
            
            r += 1
        
        return res


        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      
        min_k = +float("infinity")
        l = 1
        r = max(piles)
        while l<=r:
            t = 0
            k = l + (r-l)//2

            for p in piles:
                t += ceil(p/k)
            
            if t <= h:
                min_k = min(min_k,k)
                r = k -1
            elif t > h:
                l = k + 1
        
        return min_k if min_k != +float("infinity") else None



            
        
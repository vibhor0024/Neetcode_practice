class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0]*len(temperatures)
        
        for r in range(len(temperatures)):
            
            while stack and temperatures[r] > stack[-1][1]:
                res[stack[-1][0]] = r - stack[-1][0]
                stack.pop()
            
            stack.append([r,temperatures[r]])
        
        return res

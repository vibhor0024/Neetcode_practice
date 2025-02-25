class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = heights[0]

        for i,h in enumerate(heights):
            k = i
            while stack and stack[-1][1] > h:
                l,r = stack.pop()
                area = (i-l)*r
                max_area = max(max_area,area)
                k = l
            stack.append([k,h])
        
        for i,h in stack:
            area = (len(heights)  - i)*h
            max_area = max(max_area,area)


        return max_area
        

        
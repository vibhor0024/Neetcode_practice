# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Iterative DFS (stack)

        # stack = [[root,1]]
        # res = 0

        # while stack:
        #     node, depth = stack.pop()

        #     if node:
        #         res = max(res,depth)
        #         stack.append([node.left,depth+1])
        #         stack.append([node.right,depth+1])
        
        # return res

        #Iterative BFS (deque)

        if not root:
            return 0

        level = 0

        d = collections.deque([root])

        while d:
            
            for i in range(len(d)):
                node = d.popleft()
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            
            level += 1
        
        return level
        

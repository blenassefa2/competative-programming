# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        qu = deque([root])
        lst = []
        while qu:
            max_ = -100000000000000
            N = len(qu)
            for i in range(N):
                node = qu.popleft()
                
                if node:
                    if max_< node.val:
                        max_ = node.val
                    if node.left:
                        qu.append(node.left)
                    if node.right:
                        qu.append(node.right)
            
            lst.append(max_)
        return lst
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], count: int)->int:
        if root is None: return count
        count+=1
        res=max(self.dfs(root.left, count), self.dfs(root.right, count))
        return res
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root,res):
            if root:
                dfs(root.left,res)
                res.append(root.val)
                dfs(root.right,res)
        res=[]
        dfs(root,res)
        return res[k-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#T(N) = O(N)
#S(N) = O(H)
class Solution:
    def helper(self,root,level,ar):
        if root==None:
            return ar
        if level==len(ar):
            ar.append(root.val)
        ar=self.helper(root.right,level+1,ar)
        ar=self.helper(root.left,level+1,ar)
        return ar
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        ar=[root.val]
        ar=self.helper(root.right,1,ar)
        ar=self.helper(root.left,1,ar)
        return ar
        
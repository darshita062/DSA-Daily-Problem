class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        else:
            root = TreeNode(postorder[-1])
            mid = inorder.index(postorder[-1])
            root.left = self.buildTree(inorder[:mid],postorder[:mid])
            root.right = self.buildTree(inorder[mid+1:],postorder[mid:-1])
            return root
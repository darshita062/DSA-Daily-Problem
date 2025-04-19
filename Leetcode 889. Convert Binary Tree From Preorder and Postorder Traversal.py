class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder or not postorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        left_node = preorder[1]
        left_tree_size = postorder.index(left_node) +1
        root.left = self.constructFromPrePost(preorder[1:1+left_tree_size],postorder[:left_tree_size])
        root.right = self.constructFromPrePost(preorder[1+left_tree_size:],postorder[left_tree_size:-1])
        return root
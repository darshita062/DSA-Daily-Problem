class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def insertIntoBST(root, val):
        if not root:
            return TreeNode(val)
        tree = root
        while True:
            if val < tree.val:
                if not tree.left:
                    tree.left = TreeNode(val)
                    return root
                tree = tree.left
            else:
                if not tree.right:
                    tree.right = TreeNode(val)
                    return root
                tree = tree.right
            
        

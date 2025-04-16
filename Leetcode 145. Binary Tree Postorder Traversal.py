def postorderTraversal(root):
        if not root:
            return []
        res = []
       
        def postorder(node):
            if node.left:
                postorder(node.left)
            if node.right:
                postorder(node.right)
            res.append(node.val)
        postorder(root)
        return res
def inorderTraversal(root):
        if not root:
            return []
        array = []
        current = root
        def inorder(node):
            if node.left:
                inorder(node.left)
            array.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(current)
        return array
def preorderTraversal(root):
        if not root:
            return []
        array = []
        current = root
        def preorder(node):
            array.append(node.val)
            if node.left:
                preorder(node.left)
            if node.right:
                preorder(node.right)
        preorder(current)
        return array
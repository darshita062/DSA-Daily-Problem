def searchBST(root, val):
        tree = root
        while tree:
            if val < tree.val:
                tree = tree.left
            elif val > tree.val:
                tree = tree.right
            elif tree.val == val:
                return tree

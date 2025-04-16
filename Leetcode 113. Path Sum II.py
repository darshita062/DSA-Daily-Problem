def pathSum(root, targetSum):
        res = []
        def helper(node,curr,rem_sum):
            #base case
            if node is None:
                return
            #recursive case
            curr.append(node.val)
            if rem_sum == node.val and node.left is None and node.right is None:
                res.append(curr[:])
            else:
                helper(node.left,curr,rem_sum - node.val)
                helper(node.right,curr,rem_sum - node.val)
            #backtrack
            curr.pop()
        helper(root,[],targetSum)
        return res
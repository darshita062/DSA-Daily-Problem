def hasPathSum(root, targetSum):
    def helper(node,curr_sum):
        if node is None:
            return False
        curr_sum += node.val
        if node.left == None and node.right == None:
            return curr_sum == targetSum
        return helper(node.left,curr_sum) or helper(node.right,curr_sum)
            
    return helper(root,0)
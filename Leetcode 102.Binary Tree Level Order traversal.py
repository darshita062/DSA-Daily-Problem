from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(root):
        if root is None:
            return []
        output = []
        queue = deque([root])
        while queue:
            lenght = len(queue)
            count = 0
            curr_level_values = []
            while (count < lenght):
                curr = queue.popleft()
                curr_level_values.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                count += 1
            output.append(curr_level_values)
        return output
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# bfs modified with reversed node vals when level(s) are odd

s
class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if root is None:
            return res
        queue = [root]
        level = 0

        while len(queue) > 0:
            nodes_this_level = []
            size = len(queue)
            for i in range(size):
                popped_node = queue.pop(0)
                nodes_this_level.append(popped_node.val)
                if popped_node.left:
                    queue.append(popped_node.left)
                if popped_node.right:
                queue.append(popped_node.right)
            if level % 2 == 1:
                nodes_this_level = nodes_this_level[::-1]
            res.append(nodes_this_level)
            level += 1
        return res

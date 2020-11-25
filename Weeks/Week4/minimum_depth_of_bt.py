import sys

from Types.__tree_node__ import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = sys.maxsize

        def traverse(node, depth=1):
            nonlocal result
            if not node.left and not node.right:
                result = min(result, depth)
                return
            if node.left:
                traverse(node.left, depth + 1)
            if node.right:
                traverse(node.right, depth + 1)

        traverse(root)
        return result

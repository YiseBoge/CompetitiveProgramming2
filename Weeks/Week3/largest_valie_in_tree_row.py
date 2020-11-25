from Types.__tree_node__ import TreeNode


class Solution:
    def largestValues(self, root: TreeNode) -> list:
        results = []

        def traverse(node, level=0):
            nonlocal results
            if not node:
                return
            if len(results) <= level:
                results.append(node.val)
            else:
                results[level] = max(results[level], node.val)

            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root)
        return results

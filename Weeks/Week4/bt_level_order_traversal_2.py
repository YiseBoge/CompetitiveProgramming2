from Types.__tree_node__ import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        results = []

        def traverse(node, level=0):
            nonlocal results
            if not node:
                return
            if level >= len(results):
                results.append([])

            traverse(node.left, level + 1)
            results[level].append(node.val)
            traverse(node.right, level + 1)

        traverse(root)
        return list(reversed(results))

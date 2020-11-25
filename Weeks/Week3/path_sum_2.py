from Types.__tree_node__ import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> list:
        max_sum, results = 0, []

        def do_dfs(node, path=[]):
            nonlocal target_sum
            new_path = path + [node.val]

            if not node.left and not node.right:
                if sum(new_path) == target_sum:
                    results.append(new_path)
            if node.left:
                do_dfs(node.left, new_path)
            if node.right:
                do_dfs(node.right, new_path)

        if not root:
            return []
        do_dfs(root)
        return results

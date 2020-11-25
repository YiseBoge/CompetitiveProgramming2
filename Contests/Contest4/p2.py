from Types.__tree_node__ import TreeNode


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        discovered = []

        def traverse(node, level=0):
            nonlocal discovered
            if (node.val + level) % 2 == 0:
                return False

            if level >= len(discovered):
                discovered.append(node.val)
            elif (level % 2 == 0 and node.val <= discovered[level]) or (
                    level % 2 != 0 and node.val >= discovered[level]):
                return False
            else:
                discovered[level] = node.val

            result = True
            if node.left:
                result = result and traverse(node.left, level + 1)
            if node.right:
                result = result and traverse(node.right, level + 1)
            return result

        return traverse(root)

from Types.__tree_node__ import TreeNode


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: list) -> list:
        index, impossible = 0, False
        result = []

        def traverse(node):
            nonlocal voyage, index, result, impossible
            if index >= len(voyage) or node.val != voyage[index]:
                impossible = True
                return

            index += 1
            if (index < len(voyage)
                    and node.left
                    and node.left.val != voyage[index]):
                node.left, node.right = node.right, node.left
                result.append(node.val)

            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(root)
        return [-1] if impossible else result

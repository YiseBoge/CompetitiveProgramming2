from Types.__tree_node__ import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        if root:
            self.stack.append(root)
            self.fillLeft()

    def fillLeft(self):
        current = self.stack[-1]
        while current.left:
            self.stack.append(current.left)
            current = self.stack[-1]

    def next(self) -> int:
        current = self.stack.pop()
        if current.right:
            self.stack.append(current.right)
            self.fillLeft()
        return current.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

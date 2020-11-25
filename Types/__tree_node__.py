# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        returnable = "Node{val=" + str(self.val) + ", left=" + str(self.left) + ", right=" + str(self.right) + "}"
        return returnable

class Node:
    def __init__(self, val=None, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

    def __str__(self):
        returnable = str(self.val) + " -> " + str(self.children)
        return returnable


class Employee:
    def __init__(self, id: int, importance: int, subordinates: list):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

    def __str__(self):
        returnable = "[" + str(self.id) + ", " + str(self.importance) + ", " + str(self.subordinates) + "]"
        return returnable

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

    def __str__(self):
        returnable = str(self.val) + " -> " + str(self.next)
        return returnable

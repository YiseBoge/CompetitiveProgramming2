from Types.__list_node__ import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        space = 0
        handle = node = backup = ListNode(None)
        handle.next = head

        while node.next:
            if space >= n:
                backup = backup.next
            else:
                space += 1
            node = node.next

        backup.next = backup.next.next
        return handle.next

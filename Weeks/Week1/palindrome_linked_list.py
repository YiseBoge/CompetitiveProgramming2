import math

from Types.__list_node__ import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length, node = 0, head
        while node:
            length += 1
            node = node.next

        center = math.ceil(length / 2)
        node = head
        while center:
            node = node.next
            center -= 1

        current, forward, tail = node, None, None
        while current:
            forward = current.next
            current.next = tail
            tail = current
            current = forward

        for i in range(length // 2):
            if head is None or tail is None or head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True

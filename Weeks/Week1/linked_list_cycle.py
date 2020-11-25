import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    node, visited = head, set()
    while node:
        if node in visited:
            return True
        visited.add(node)
        node = node.next
    return False


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        l_list_count = int(input())

        l_list = SinglyLinkedList()

        for _ in range(l_list_count):
            l_list_item = int(input())
            l_list.insert_node(l_list_item)

        extra = SinglyLinkedListNode(-1)
        temp = l_list.head

        for i in range(l_list_count):
            if i == index:
                extra = temp

            if i != l_list_count - 1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(l_list.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()

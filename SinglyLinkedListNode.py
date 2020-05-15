def get_test_head_node():
    node2 = SinglyLinkedListNode(1)
    node3 = SinglyLinkedListNode(2)
    node4 = SinglyLinkedListNode(2)
    node5 = SinglyLinkedListNode(3)
    node6 = SinglyLinkedListNode(4)

    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    return node2


class SinglyLinkedListNode:
    next = None

    def __init__(self, _data):
        self.data = _data

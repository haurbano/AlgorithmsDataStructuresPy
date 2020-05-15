from SinglyLinkedListNode import SinglyLinkedListNode


def insertNodeAtTail(head, data):
    newHead = head
    while newHead.next is not None:
        newHead = newHead.next
    newHead.next = SinglyLinkedListNode(data, None)
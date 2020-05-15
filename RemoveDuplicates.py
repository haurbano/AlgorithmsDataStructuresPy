from SinglyLinkedListNode import SinglyLinkedListNode


def removeDuplicates(head_node):
    nodes_map = {}
    node = head_node
    while node is not None:
        nodes_map[str(node.data)] = node.data
        node = node.next

    values = list(nodes_map.values())
    head_node = SinglyLinkedListNode(values[0])
    current_node = head_node
    for index in range(1, len(values)):
        next_node = SinglyLinkedListNode(values[index])
        current_node.next = next_node
        current_node = next_node

    return head_node

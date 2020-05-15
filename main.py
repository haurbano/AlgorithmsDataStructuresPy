from SinglyLinkedListNode import get_test_head_node
from RemoveDuplicates import removeDuplicates

head_node = removeDuplicates(get_test_head_node())
node = head_node
while node is not None:
    print(node.data)
    node = node.next

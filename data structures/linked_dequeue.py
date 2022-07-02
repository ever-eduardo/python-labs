#
# Double Ended Queue - ADT
# Doubly Linked List Implementation
#


class Node:
    """
    Node represents a node of a doubly linked list.
    """
    __slots__ = 'data', 'prev', 'next'

    def __init__(self, data, prev, next_node):
        """
        Initializes a Node.
        :param data: Any
        :param prev: Node
        :param next_node: Node
        """
        self.data = data
        self.prev = prev
        self.next = next_node

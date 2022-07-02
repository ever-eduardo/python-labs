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


class LinkedDequeue:
    """
    Double ended queue ADT.
    A Doubly Linked List Implementation.
    """

    def __init__(self):
        """
        Creates an empty dequeue.
        """
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0
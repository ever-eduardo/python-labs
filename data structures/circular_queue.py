#
# Circular Queue FIFO ADT
# Circularly Linked List Implementation.
#

class Node:
    """
    Class modeling a Node for a linked style ADT.
    """
    __slots__ = 'data', 'next'

    def __init__(self, data, next_node=None):
        """
        Initializes the Node.
        :param data: Any
        :param next_node: Any
        """
        self.data = data
        self.next = next_node


class CircularQueue:
    """
    Queue implementation using a circular singly linked list.
    """
    __slots__ = 'tail', 'size'

    def __init__(self):
        self.tail = None
        self.size = 0

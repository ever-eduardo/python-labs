#
# Singly Linked List
# ADT
#


class Node:
    """
    Class modeling a Node of a singly linked ADT.
    """
    __slots__ = 'data', 'next'

    def __init__(self, data, next_node):
        """
        Initializes the Node first state.
        :param data: Any
        :param next_node: Any | None
        """
        self.data = data
        self.next = next_node


class LinkedList:
    """
    Class modeling a singly linked list.
    """
    __slots__ = 'head', 'size'

    def __init__(self):
        """
        Initializes a list to its initial state with zero nodes and size of zero.
        """
        self.head = Node
        self.size = 0

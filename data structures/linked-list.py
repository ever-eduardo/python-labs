#
# Singly Linked List
# ADT
#


class Node:
    """
    Class modeling a Node of a singly linked ADT.
    """
    __slots__ = 'data', 'next'

    def __init__(self, data, next_node=None):
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
    __slots__ = 'head', 'tail', 'size'

    def __init__(self):
        """
        Initializes a list to its initial state with head and tail to none and size to zero.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """
        :return: The number of elements in the list.
        """
        return self.size

    def is_empty(self):
        """
        :return: True when the list has no nodes.
        """
        return self.size == 0

    def push_front(self, data):
        """
        Pushes a node at the front-end of the list.
        :param data: Any
        :return: None
        """
        if self.tail is None and self.head is None:
            node = Node(data)
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
            self.size += 1

    def push_back(self, data):
        """
        Pushes a node at the back-end of the list.
        :param data: Any
        :return: None
        """

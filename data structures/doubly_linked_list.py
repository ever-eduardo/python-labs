#
# Doubly Linked List - ADT
# This implementation uses two sentinels:
# The header and the trailer nodes.
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


class DoublyLinkedList:
    """
    A Doubly Linked List Implementation.
    """
    def __init__(self):
        """
        Creates an empty list.
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

    def insert_between(self, data, predecessor, successor):
        """
        Inserts a new node between two existing ones.
        :param data: Any
        :param predecessor: Node
        :param successor: Node
        :return: The new node.
        """
        node = Node(data, predecessor, successor)
        predecessor.next = node
        successor.prev = node
        self.size += 1
        return node

    def delete_node(self, node):
        """
        Deletes a node from the list.
        :param node: Node
        :return: The data contained in the param node.
        """
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        data = node.data
        node.prev = node.next = node.data = None
        return data

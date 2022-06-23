#
# Stack ADT
# Singly List Implementation.
#


class Node:
    """
    Class modeling a Node for linked style ADTs.
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


class LinkedStack:
    """
    Class modeling a Stack with a singly linked list implementation.
    """
    __slots__ = 'head', 'size'

    def __init__(self):
        """
        Initializes a stack to its initial state with head to none and size to zero.
        """
        self.head = None
        self.size = 0

    def __len__(self):
        """
        :return: The number of elements of the stack.
        """
        return self.size

    def is_empty(self):
        """
        :return: True when the stack has no nodes.
        """
        return self.size == 0

    def push(self, data):
        """
        Pushes a node onto the stack.
        :param data: Any
        :return: None
        """
        self.head = Node(data, self.head)
        self.size += 1

    def pop(self):
        """
        Removes the element at the top of the stack.
        Raise an exception if the stack is empty.
        :return: The data on top of the stack.
        """
        if self.is_empty():
            raise Exception("Attempting to pop an element from an empty LinkedStack")
        node = self.head
        data = node.data
        self.head = self.head.next
        self.size -= 1
        node.next = None
        return data
    
    def peek(self):
        """
        A observer method of the element at the top of the stack.
        Raise an exception if the stack is empty.
        :return: The data of the element on top of the stack.
        """
        if self.is_empty():
            raise Exception("Attempting to read the top element from an empty LinkedStack")
        return self.head.data


#
# Linked Queue FIFO ADT
# Singly List Implementation.
#


class Node:
    """
    Class modeling a Node for linked style ADT.
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


class LinkedQueue:
    """
    Class modeling a Queue with a singly linked list implementation.
    """
    __slots__ = 'head', 'tail', 'size'

    def __init__(self):
        """
        Initializes a queue to its initial state with head and tail to None and size to zero.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """
        :return: The number of elements in the queue.
        """
        return self.size

    def is_empty(self):
        """
        :return: True when the queue has no nodes.
        """
        return self.size == 0

    def enqueue(self, data):
        """
        Enqueues a node.
        :param data: Any
        :return: None
        """
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def dequeue(self):
        """
        Removes the first element of the queue.
        Raises an exception when the queue is empty.
        :return: The data of the first element of the queue.
        """
        if self.is_empty():
            raise Exception("Attempting to dequeue an element from an empty LinkedQueue")
        node = self.head
        data = node.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        node.next = None
        return data
    
    def first(self):
        """
        A observer method of the data of the first element of the queue.
        Raise an exception if the queue is empty.
        :return: The data of the first element of the queue.
        """
        if self.is_empty():
            raise Exception("Attempting to read the first element from an empty LinkedQueue")
        return self.head.data


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
        """
        Initializes an empty Queue.
        """
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

    def first(self):
        """
        Allows to peek the data of the first element of the Queue.
        Raises an exception when the Queue is empty.
        :return: The data of the first element of the Queue.
        """
        if self.is_empty():
            raise Exception("Attempting to peek an element from an empty queue")
        return self.tail.next.data

    def enqueue(self, data):
        """
        Adds an element to the tail of the Queue.
        :param data: Any
        :return: None
        """
        node = Node(data)
        if self.is_empty():
            node.next = node
        else:
            node.next = self.tail.next
            self.tail.next = node
        self.tail = node
        self.size += 1

    def dequeue(self):
        """
        Removes the first element of the Queue.
        Raises an exception when the queue is empty.
        :return: The data of the first element of the Queue.
        """
        if self.is_empty():
            raise Exception("Attempting to dequeue an element from an empty Queue")
        current_head = self.tail.next
        data = current_head.data
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = current_head.next
        current_head.next = None
        self.size -= 1
        return data

    def rotate(self):
        """
        Translates the front element to the back of the Queue.
        :return: None
        """
        if self.size > 0:
            self.tail = self.tail.next
    
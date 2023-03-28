#!/usr/bin/python3

"""Class Node that defines a node of a singly linked list"""


class Node:
    """Private instance attribute: data"""
    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""Class SinglyLinkedList that defines a singly linked list"""


class SinglyLinkedList:
    """Private instance attribute: head"""
    def __init__(self):
        """Simple instantiation"""
        self.__head = None

    def __str__(self):
        """Should be printable"""
        current = self.__head
        string = ""
        while current:
            string += str(current.data) + "\n"
            current = current.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """Public instance method: def sorted_insert(self, value)"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

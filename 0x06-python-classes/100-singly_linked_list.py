#!/usr/bin/python3
"""
Module: 7-linked_list
Defines a Node class and a SinglyLinkedList class
"""


class Node:
    """
    Node class that defines a node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance with data and next_node.

        Args:
            data: The data of the node (must be an integer).
            next_node: The next node in the linked list (must be a Node or None).

        Raises:
            TypeError: If data is not an integer or next_node is not a Node or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for setting the data of the node.

        Args:
            value: The data to set.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving the next_node of the node.

        Returns:
            Node or None: The next_node of the node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the next_node of the node.

        Args:
            value: The next_node to set.

        Raises:
            TypeError: If next_node is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class that defines a singly linked list
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance with an empty head.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value: The value to insert into the list.

        Note:
            This method modifies the linked list in place.
        """
        new_node = Node(value)
        if not self.head or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()


if __name__ == "__main__":
    # Example usage:
    linked_list = SinglyLinkedList()
    linked_list.sorted_insert(5)
    linked_list.sorted_insert(3)
    linked_list.sorted_insert(8)
    linked_list.sorted_insert(1)
    print(linked_list)


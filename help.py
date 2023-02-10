# Author: Robert Smith
# GitHub username: robertsmith2727
# Date: 11/04/2022
# Description: Creates a Linked List data structure that has multiple methods to add, remove, reverse, and
#              insert to the list. Also has to_plain_list function that returns a plain list and a contains
#              method that shows if the list contains a value. All methods use recursion.

class Node:
    """Represents a node in a linked list"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A linked list implementation of the List ADT"""

    def __init__(self):
        self._head = None

    def get_head(self):
        return self._head

    def add(self, val):
        """Calls rec_add function with current and value"""
        current = self._head
        self.rec_add(val, current)

    def rec_add(self, val, current):
        """Recursively adds a node containing val to the linked list"""
        if self._head is None:  # If the list is empty
            self._head = Node(val)
            return
        if current.next is None:
            current.next = Node(val)
            return
        return self.rec_add(val, current.next)

    def remove(self, val):
        """Calls rec_remove function with value and as additional parameters current and previous"""
        current = self._head
        previous = None
        self.rec_remove(val, current, previous)

    def rec_remove(self, val, current, previous):
        """Removes the node containing val from the linked list"""
        if self._head is None:  # If the list is empty
            return

        if self._head.data == val:  # If the node to remove is the head
            self._head = self._head.next
            return
        if current is not None and current.data != val:
            previous = current
            current = current.next
            return self.rec_remove(val, current, previous)
        if current is not None:  # If we found the value in the list
            previous.next = current.next
            return

    def contains(self, val):
        """Calls rec_contains function with value and current as an additional parameter"""
        current = self._head
        return self.rec_contains(val, current)

    def rec_contains(self, val, current):
        """Returns true if the linked list contains the given value, otherwise returns false"""
        if self._head is None:  # If the list is empty
            return bool(self._head)
        if self._head.data == val:
            return True
        if current is not None and current.data != val:
            current = current.next
            return self.rec_contains(val, current)
        if current is not None:
            return True
        else:
            return False

    def to_plain_list(self):
        """Calls rec_to_plain_list function with current as an additional parameter"""
        current = self._head
        return self.rec_to_plain_list(current)

    def rec_to_plain_list(self, current, result=None):
        """Returns a regular Python list containing the same values, in the same order, as the linked list"""
        if result is None:
            result = []
        if current is not None:
            result += [current.data]
            current = current.next
            return self.rec_to_plain_list(current, result)
        return result

    def insert(self, val, pos):
        """Calls rec_insert function with value and pos and current as an additional parameter"""
        if pos < 0:
            temp_pos = len(LinkedList.to_plain_list(self)) + pos
            pos = temp_pos
        current = self._head
        count = 1
        return self.rec_insert(val, pos, current, count)

    def rec_insert(self, val, pos, current, count):
        """Inserts a node containing val into the linked list at position pos"""
        if self._head is None:  # If the list is empty
            self.add(val)
            return

        if pos == 0:  # If it starts at the first index
            temp = self._head
            self._head = Node(val)
            self._head.next = temp
            return

        if pos > count and current.next is None:  # If the pos is greater that the last index
            current.next = Node(val)
            return
        if count == pos:
            following = current.next
            current.next = Node(val)
            current.next.next = following
            return
        current = current.next
        return self.rec_insert(val, pos, current, count+1)

    def reverse(self):
        """Calls rec_reverse function with current, previous, and following as additional parameters"""
        current = self._head
        previous = None
        following = None
        return self.rec_reverse(current, previous, following)

    def rec_reverse(self, current, previous, following):
        """Returns the reverse of the linked list"""
        if current is None:
            return
        if current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
            self._head = previous
        return self.rec_reverse(current, previous, following)


# Name: Robert Smith
# OSU Email: Smithro8@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment: 3
# Due Date: 02/13/2023
# Description: Implements a stack SDT using singly linked nodes
#              methods for push, pop, and top

from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------
    def push(self, value: object) -> None:
        """
        Pushes value to the top of the stack, which is the head of the LL
        """
        # creates head as first node
        if self.is_empty() is True:
            self._head = SLNode(value)
            return
        # creates node and holds head as temp
        new_node = SLNode(value)
        temp_node = self._head
        # assigns new to head and old to next
        self._head = new_node
        self._head.next = temp_node

    def pop(self) -> object:
        """
        Removes the top of the stack, which is the head of the LL
        """
        # if empty
        if self.is_empty() is True:
            raise StackException
        # saves value being popped
        value = self._head.value
        # points head to the next val
        self._head = self._head.next
        return value

    def top(self) -> object:
        """
        Returns the top of the stack, which is the head of the LL
        """
        # if empty
        if self.is_empty() is True:
            raise StackException
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------
if __name__ == "__main__":
    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)
    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))
    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)

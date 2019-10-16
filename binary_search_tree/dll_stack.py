from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size is not 0:
            deleted = self.storage.remove_from_tail()
            self.size -= 1
            return deleted
        else:
            return None

    def len(self):
        return self.storage.__len__()
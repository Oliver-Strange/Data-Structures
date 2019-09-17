from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if len(self.storage) is not 0:
            deleted = self.storage.remove_from_head()
            self.size -= 1
            return deleted
        else:
            return None

    def len(self):
        return self.size

# Create Linked List with these methods
# print all linked - lists
# enqueue(self, item) add to last
# dequeue(self) remove head thanos LOL
# length
# def contains(self, value):


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def display(self):
        if not self.head:
            return -1
        else:
            elems = []
            old_head = self.head
            while old_head:
                elems.append(old_head.value)
                old_head = self.head.next
            return elems
        pass

    def enqueue(self, item):

        pass

    def dequeue(self, item):
        pass

    def len(self, item):
        pass

    def contains(self, item):
        pass


test = LinkedList()
print(test.display())

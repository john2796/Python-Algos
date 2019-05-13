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
        self.tail = None
        self.size = 0

    def display(self):
        if not self.head and not self.tail:
            return None
        else:
            elems = []
            cur = self.head
            while cur:
                elems.append(cur.value)
                cur = cur.next
            return elems

        pass

    def enqueue(self, item):
        new_node = Node(item)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return

    def dequeue(self):
        if not self.head and not self.tail:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return

    def len(self):
        return self.size

    def contains(self, target):
        if not self.head and not self.tail:
            return None
        else:
            cur = self.head
            while cur:
                cur = cur.next
                if target == cur.value:
                    return True
                else:
                    return False


test = LinkedList()
print(test.enqueue(1))
print(test.enqueue(2))
print(test.enqueue(3))
print(test.enqueue(4))
print(test.enqueue(5))
print(test.contains(6), 'contains -->')
print(test.display())
print(test.len())

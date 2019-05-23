

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def display(self):
        if not self.head and not self.tail:
            return []
        else:
            elem = []
            current = self.head
            print(
                f"head: {self.head.value} tail: {self.tail.value} size: {self.size}")
            while current:
                elem.append(current.value)
                current = current.next
            return elem

    def add_to_head(self, item):
        new_node = Node(item)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            current.prev = new_node
            self.head = new_node
            self.head.next = current
            self.head.prev = None
        self.size += 1
        return self.head

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.tail and not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            current.next = new_node
            self.tail = new_node
            self.tail.prev = current
        self.size += 1
        return self.head
# 3 cases for removing
# 1 if there's no Node
# 2 if there's only one node
# 3 if there's more this Node

    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head.next
            self.head = current
            self.head.prev = None
        self.size -= 1
        return self.head

    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.tail.prev
            self.tail = current
            self.tail.next = None
        self.size -= 1
        return self.head

    def move_to_end(self, item):
        if not self.head and not self.tail:
            self.add_to_head(item)
        if self.tail == self.head:
            self.add_to_tail(item)
        else:
            current = self.head
            while current:
                if current.value == item:
                    self.delete(current.value)
                    self.add_to_tail(item)
                    return
            current = current.next

    def move_to_front(self, item):
        if not self.head and not self.tail:
            self.add_to_head(item)
        if self.tail == self.head:
            self.add_to_head(item)
        else:
            current = self.head
            while current.value != item:
                current = current.next
                self.delete(item)
                self.add_to_head(item)
            return

    def delete(self, target):
        if not self.head and not self.tail:
            return None
        if self.tail == self.head:
            self.head = None
            self.tail = None
        if self.head.value == target:
            self.remove_from_head()
        elif self.tail.value == target:
            self.remove_from_tail()
        else:
            current = self.head
            while current:
                current = current.next
                if current.value == target:
                    nxt = current.next
                    prev = current.prev
                    current = None
                    nxt.prev = prev
                    prev.next = nxt
                    return


test = DoublyLinkedList()
test.add_to_head(3)
test.add_to_head(2)
test.add_to_head(1)
test.add_to_tail(4)
# print(test.move_to_front(2), '<- move-to-end')
print(test.move_to_end(1), '<- move-to-end')
print(test.display())

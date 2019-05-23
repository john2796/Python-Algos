

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
            while current:
                elem.append(current.value)
                current = current
            return elem

    def add_to_head(self, item):
        new_node = Node(item)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            cur = self.head
            self.head = new_node
            self.head.next = cur
        self.size += 1
        return

    def add_to_tail(self):
        pass

    def remove_from_head(self):
        pass

    def remove_from_tail(self):
        pass

    def remove_to_front(self):
        pass

    def remove_to_end(self):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass


test = DoublyLinkedList()
test.add_to_head(1)
test.add_to_head(4)
test.add_to_head(23)
print(test.display())

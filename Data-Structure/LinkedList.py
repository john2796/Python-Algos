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

    def add_to_first(self, item):
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

    def remove_last(self):
        if not self.head and not self.tail:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            cur = self.head
            prev = None
            while cur != self.tail:
                prev = cur
                cur = cur.next

            prev.next = None
            self.tail = prev
            self.size -= 1
            return cur.value

    # def add_n(self, n):
    #     if not self.head and not self.tail:
    #         return None
    #     if self.head == self.tail:
    #         return self.enqueue(n)
    #     if n == self.head.value:
    #         return self.add_to_first(n)
    #     elif n == self.tail.value:
    #         return self.enqueue(n)
    #     else:
    #         new_node = Node(n)
    #         cur = self.head
    #         prev = None
    #         while cur.value != n:
    #             prev = cur
    #             cur = cur.next

    #     self.size += 1
    #     return

    def remove_n(self, n):
        if not self.head and not self.tail:
            return None
        if self.head == self.tail:
            return self.dequeue()
        if n == self.head.value:
            return self.dequeue()
        elif n == self.tail.value:
            return self.remove_last()
        else:
            cur = self.head
            prev = None
            while cur.value != n:
                prev = cur
                cur = cur.next

            prev.next = cur.next
            self.size -= 1
            return cur.value

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


print(test.display())
print(test.len())

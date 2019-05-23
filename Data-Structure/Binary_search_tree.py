class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.max = None

    def insert(self, value):
        if value < self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def print(self):  # inorder traversal
        if self.left is not None:
            self.left.print()
        print(f"{self.data}")
        if self.right is not None:
            self.right.print()

    def contains(self, target):  # recursive
        print(self.data, target)
        if self.data == target:
            print(True)
            return True
        if target < self.data:
            if self.left is None:
                print(False)
                return False
            else:
                self.left.contains(target)
        else:
            if self.right is None:
                print(False)
                return False
            else:
                self.right.contains(target)

    # def get_max(self): get max iterative
    #     current = self
    #     while current.right is not None:
    #         current = current.right
    #     return current.data

    def get_max(self):  # recursive get max
        if self is None:
            return -1
        elif self.right == None:
            return self.data
        return self.right.get_max()

    def get_min(self):  # recursive get min
        if self is None:
            return -1
        elif self.left == None:
            return self.data
        return self.left.get_min()


test = Node(4)
test.insert(2)
test.insert(5)
test.insert(3)
test.insert(12)
test.insert(32)
print(test.contains(3))
print(test.get_max(), '<--max')
print(test.get_min(), '<--min')

print(test.print())

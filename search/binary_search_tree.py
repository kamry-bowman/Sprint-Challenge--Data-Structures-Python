from collections import deque


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        stack = [self]
        while stack:
            current = stack.pop()
            cb(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def breadth_first_for_each(self, cb):
        queue = deque()
        queue.appendleft(self)
        while queue:
            current = queue.pop()
            cb(current.value)
            if current.left:
                queue.appendleft(current.left)
            if current.right:
                queue.appendleft(current.right)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value


example = BinarySearchTree(5)
example.insert(3)
example.insert(2)
example.insert(6)
example.insert(7)

example.breadth_first_for_each(print)



class Node:
    left = None
    right = None
    balance = 0

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent


class Tree:
    head = None

    def tree_insert(self, data):

        current = self.head
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        if self.head is None:
            self.head = Node(data)
        elif data <= parent.data:
            current = Node(data, parent)
            parent.left = current
        else:
            current = Node(data, parent)
            parent.right = current

        while parent is not None:
            parent.balance += (-1 if current == parent.left else 1)
            if (parent.balance == 0):
                break
            current = parent
            parent = parent.parent
        


    def tree_search(self, data):
        current = self.head
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None
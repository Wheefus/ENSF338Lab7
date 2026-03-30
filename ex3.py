class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.balance = 0


class Tree:
    def __init__(self):
        self.head = None

    # ---------------- ROTATIONS ---------------- #

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left

        if new_root.left:
            new_root.left.parent = node

        new_root.parent = node.parent

        if node.parent is None:
            self.head = new_root
        elif node == node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root

        new_root.left = node
        node.parent = new_root

        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right

        if new_root.right:
            new_root.right.parent = node

        new_root.parent = node.parent

        if node.parent is None:
            self.head = new_root
        elif node == node.parent.right:
            node.parent.right = new_root
        else:
            node.parent.left = new_root

        new_root.right = node
        node.parent = new_root

        return new_root

    # ---------------- REBALANCE ---------------- #

    def _rebalance(self, node):
        # RIGHT HEAVY
        if node.balance > 1:
            if node.right.balance >= 0:
                print("Case #3a: adding a node to an outside subtree")
                new_root = self._rotate_left(node)

                # reset balances
                node.balance = 0
                new_root.balance = 0

            else:
                print("Case 3b not supported")

        # LEFT HEAVY
        elif node.balance < -1:
            if node.left.balance <= 0:
                print(f"Inserted {node.data}: Case #3a: adding a node to an outside subtree")
                new_root = self._rotate_right(node)

                # reset balances
                node.balance = 0
                new_root.balance = 0

            else:
                print(f"Inserted {node.data}: Case 3b not supported")

    # ---------------- INSERT ---------------- #

    def tree_insert(self, data):
        current = self.head
        parent = None
        pivot = None

        # Find insertion point + pivot
        while current is not None:
            if current.balance != 0:
                pivot = current
            parent = current
            current = current.left if data <= current.data else current.right

        new_node = Node(data, parent)

        # Empty tree
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data}: Case #1: Pivot not detected")
            return

        # Attach node
        if data <= parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        # Case 1 / Case 2 detection
        if pivot is None:
            print(f"Inserted {data}: Case #1: Pivot not detected")
        else:
            is_shorter = (
                (pivot.balance == -1 and data > pivot.data) or
                (pivot.balance == 1 and data <= pivot.data)
            )
            if is_shorter:
                print(f"Inserted {data}: Case #2: A pivot exists, and a node was added to the shorter subtree")

        # Update balances upward
        curr = new_node
        p = parent

        while p is not None:
            if curr == p.left:
                p.balance -= 1
            else:
                p.balance += 1

            # stop if balanced
            if p.balance == 0:
                break

            # rebalance if needed
            if p.balance < -1 or p.balance > 1:
                self._rebalance(p)
                break

            curr = p
            p = p.parent


# ---------------- TESTING ---------------- #

if __name__ == "__main__":
    print("\n--- Case 1 & 2 Tests ---")
    t = Tree()
    t.tree_insert(10)
    t.tree_insert(5)
    t.tree_insert(15)

    print("\n--- Case 3a (RR) ---")
    t = Tree()
    t.tree_insert(10)
    t.tree_insert(20)
    t.tree_insert(30)  # outside → 3a

    print("\n--- Case 3a (LL) ---")
    t = Tree()
    t.tree_insert(30)
    t.tree_insert(20)
    t.tree_insert(10)  # outside → 3a

    print("\n--- Case 3b (Not Supported) ---")
    t = Tree()
    t.tree_insert(10)
    t.tree_insert(30)
    t.tree_insert(20)  # inside → 3b
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

    # ---------------- SINGLE ROTATIONS ---------------- #

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

    # ---------------- DOUBLE ROTATIONS (NEW) ---------------- #

    def _lr_rotate(self, node):
        # Left-Right: rotate left on left child, then right on node
        self._rotate_left(node.left)
        return self._rotate_right(node)

    def _rl_rotate(self, node):
        # Right-Left: rotate right on right child, then left on node
        self._rotate_right(node.right)
        return self._rotate_left(node)

    # ---------------- REBALANCE ---------------- #

    def _rebalance(self, node):
        # RIGHT HEAVY
        if node.balance > 1:
            if node.right.balance >= 0:
                print(f"Inserted {node.data}: Case #3a: adding a node to an outside subtree (RR)")
                new_root = self._rotate_left(node)

                node.balance = 0
                new_root.balance = 0

            else:
                print(f"Inserted {node.data}: Case #3b: adding a node to an inside subtree (RL)")
                new_root = self._rl_rotate(node)

                # Fix balances (simplified but works for insertion cases)
                new_root.balance = 0
                if new_root.left:
                    new_root.left.balance = 0
                if new_root.right:
                    new_root.right.balance = 0

        # LEFT HEAVY
        elif node.balance < -1:
            if node.left.balance <= 0:
                print("Case #3a: adding a node to an outside subtree (LL)")
                new_root = self._rotate_right(node)

                node.balance = 0
                new_root.balance = 0

            else:
                print("Case #3b: adding a node to an inside subtree (LR)")
                new_root = self._lr_rotate(node)

                new_root.balance = 0
                if new_root.left:
                    new_root.left.balance = 0
                if new_root.right:
                    new_root.right.balance = 0

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

        # Case 1 / Case 2
        if pivot is None:
            print(f"Inserted {data}: Case #1: Pivot not detected")
        else:
            is_shorter = (
                (pivot.balance == -1 and data > pivot.data) or
                (pivot.balance == 1 and data <= pivot.data)
            )
            if is_shorter:
                print(f"Inserted {data}: Case #2: shorter subtree")

        # Update balances upward
        curr = new_node
        p = parent

        while p is not None:
            if curr == p.left:
                p.balance -= 1
            else:
                p.balance += 1

            if p.balance == 0:
                break

            if p.balance < -1 or p.balance > 1:
                self._rebalance(p)
                break

            curr = p
            p = p.parent


# ---------------- TESTING ---------------- #

if __name__ == "__main__":

    print("\n--- Case 3b (LR) ---")
    t = Tree()
    t.tree_insert(30)
    t.tree_insert(10)
    t.tree_insert(20)  # LR rotation

    print("\n--- Case 3b (RL) ---")
    t = Tree()
    t.tree_insert(10)
    t.tree_insert(30)
    t.tree_insert(20)  # RL rotation

    print("\n--- Mixed Test ---")
    t = Tree()
    for x in [10, 20, 30, 25, 5, 15]:
        t.tree_insert(x)
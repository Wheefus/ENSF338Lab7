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

    def _rebalance(self, node):
        print("Case 3 not supported") # As per requirement
        if node.balance > 1:
            if node.right.balance < 0:
                self._rotate_right(node.right)
            self._rotate_left(node)
        elif node.balance < -1:
            if node.left.balance > 0:
                self._rotate_left(node.left)
            self._rotate_right(node)
        node.balance = 0
        if node.parent: node.parent.balance = 0

    def tree_insert(self, data):
        current = self.head
        parent = None
        pivot = None
        
        # 1. Find insertion point and identify the Pivot Node
        while current is not None:
            if current.balance != 0:
                pivot = current
            parent = current
            current = current.left if data <= current.data else current.right

        new_node = Node(data, parent)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data}: Case #1: Pivot not detected")
            return

        if data <= parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        # 2. Identify Case 1 and Case 2
        if pivot is None:
            print(f"Inserted {data}: Case #1: Pivot not detected")
        else:
            # Check if insertion is in the shorter subtree
            is_shorter = (pivot.balance == -1 and data > pivot.data) or \
                         (pivot.balance == 1 and data <= pivot.data)
            if is_shorter:
                print(f"Inserted {data}: Case #2: A pivot exists, and a node was added to the shorter subtree")

        # 3. Update balances (Existing logic)
        curr = new_node
        p = parent
        while p is not None:
            p.balance += (-1 if curr == p.left else 1)
            if p.balance == 0:
                break
            if p.balance < -1 or p.balance > 1:
                self._rebalance(p)
                break
            curr = p
            p = p.parent

# --- Testing ---
t = Tree()

# Test 1: Case 1 (No pivot exists)
t.tree_insert(10) 
# Root is balance 0, inserting 5 makes root the only node.

# Test 2: Case 1 again (Pivot still doesn't exist because 10's balance was 0)
t.tree_insert(5)  

# Test 3: Case 2 (Pivot is 10 [bal -1], we insert 15 into the shorter [right] side)
t.tree_insert(15) 

# Test 4: Case 3 (Pivot is 10 [bal 0], insert 20 -> 10 bal 1. Then insert 25 -> 10 bal 2)
t.tree_insert(20)
t.tree_insert(25) # Should trigger Case 3

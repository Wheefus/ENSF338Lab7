import sys
sys.setrecursionlimit(200000)
import random
import timeit
import matplotlib.pyplot as plt

class Node:
    left = None
    right = None
    balance = 0

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent


class Tree:
    head = None

    def insert(self, data):

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
        


    def search(self, data):
        current = self.head
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None


    def largest_balance(self, cur:Node):
        if cur == None:
            return 0
        
        left_largest = self.largest_balance(cur.left)
        right_largest = self.largest_balance(cur.right)

        largest = abs(cur.balance) if abs(cur.balance) > left_largest else left_largest
        largest = largest if largest > right_largest else right_largest

        return largest
        

        

def main():
    arr = [x for x in range(1000)]
    times = []
    largest_balances = []
    for task in range(1000):
        random.shuffle(arr)
        tree = Tree()
        for val in arr:
            tree.insert(val)

        perf_time = 0
        for val in arr:
            perf_time += timeit.timeit(lambda: tree.search(val), number=10)/10
        perf_time /= 1000

        times.append(perf_time)

        largest_balances.append(tree.largest_balance(tree.head))

    plt.figure(1)
    plt.scatter(largest_balances, times)
    plt.xlabel('Absolute Balance')
    plt.ylabel('average time (s)')
    plt.title('Absolute Balance vs time for binary tree')
    plt.savefig('1.1.png')
    plt.show()

main()

        
        
            


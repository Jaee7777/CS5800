from math import log, factorial


def comb(n, h):
    return factorial(n) // (factorial(h) * factorial(n - h))


class Node:
    # initialize a node.
    def __init__(self, value=None):
        self.parent = None
        self.child = []
        self.value = value
        self.index = 0

    # create a connection between two nodes. 'other_node' is a child of 'self'.
    def connect(self, other_node):
        self.child.append(other_node)
        other_node.parent = self
        return


class Tree:
    def __init__(self):
        self.root = Node()


class BinomialTree:
    def __init__(self, array):
        # if the input's length is not 2^n, fill remaining elements to be None.
        if log(len(array), 2) - int(log(len(array), 2)) != 0:
            N_total = 2 ** round(log(len(array), 2) + 0.5)
            self.array = array
            for i in range(0, N_total - len(array)):
                self.array.append(None)
        # otherwise, simply assign array directly into the tree.
        else:
            self.array = array

        self.len = len(self.array)
        self.depth = int(log(self.len, 2))  # make sure the depth is an integer

        # create empty nodes.
        self.nodes = [Node() for i in range(self.len)]

        # make connections to the empty nodes to create a tree structure.
        len_level = self.len
        while len_level > 1:
            for i in range(0, len_level // 2):
                self.nodes[i].connect(self.nodes[i + len_level // 2])
            len_level = len_level // 2

        # assign a root node.
        self.root = self.nodes[0]

        # assign values to the nodes.
        i = 0
        for n in self.array:
            self.nodes[i].value = n
            i += 1

    def update(self):
        # update attrs based on the node structure.
        self.depth = 0
        cursor = self.root
        while cursor.child != []:
            self.depth += 1
            cursor = cursor.child[-1]
        self.len = 2**self.depth

        self.array = [self.root]
        for h in range(0, self.depth):
            pass
        return

    def merge(self, other_tree):
        if self.root.value <= other_tree.root.value:
            self.root.child.append(other_tree.root)
            other_tree.root.parent = self.root
            return self
        else:
            other_tree.root.child.append(self.root)
            self.root.parent = other_tree.root
            return other_tree

    def deleteMin(self):
        print("hi")
        pass

    def insert(self, n):
        pass

    def HeapOrder(self):
        pass


if __name__ == "__main__":
    input = [7, 8, 12, 5, 2, 0, 0, 0, 0]
    a = BinomialTree(input)
    print(a.root.parent, a.root.child)
    print(a.root.value, a.nodes[1].value)
    print(a.len)
    print(a.array)
    a.update()
    print(a.array)

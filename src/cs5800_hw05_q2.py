import math


class Node:
    def __init__(self, value):
        self.parent = None
        self.child = None
        self.value = value
        self.index = 0


class BinomialTree:
    def __init__(self, tree):
        self.tree = tree
        self.root = tree[0]
        self.depth = int(math.log(len(tree), 2))
        # create corresponding nodes for each element.
        self.nodes = []
        [self.nodes.append(Node(x)) for x in self.tree]
        self.junk = []

    # connect each node to a binomial tree from by running this .
    def connect_nodes(self):
        self.nodes[1].parent = self.nodes[0].index
        for x in range(0, self.depth):
            self.junk.append(x)
        return

    def merge(self, other_nodes):
        if self.root <= other_nodes.root:
            other_nodes[0].parent = self.nodes[0].index
        else:
            self.nodes[0].parent = other_nodes[0].index
        pass

    def deleteMin(self):
        print("hi")
        pass

    def insert(self, n):
        pass

    def HeapOrder(self):
        pass


if __name__ == "__main__":
    input = [7, 8, 12, 13]
    x = BinomialTree(input)
    print(x, x.depth, x.nodes, x.root, x.depth)
    print(x.junk)
    x.connect_nodes
    print(x.junk)
    print(x.nodes[0].parent)

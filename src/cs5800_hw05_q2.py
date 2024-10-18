from math import log, factorial
from copy import deepcopy


# function for the number of combinations.
def comb(n, h):
    return factorial(n) // (factorial(h) * factorial(n - h))


class Node:
    # initialize a node. default value is None.
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

    # create an empty binomial tree with a given depth. self is the root node.
    def create_empty_BinomialTree(self, depth):
        tree_result = [self, Node()]  # initialize with tree of h = 1.
        self.connect(tree_result[-1])  # make initial connection between nodes.
        for h in range(1, depth):
            tree_other = deepcopy(tree_result)  # create a deep copy.
            tree_result[0].connect(tree_other[0])  # connect the root nodes.
            tree_result = self.sort_empty_tree(tree_result, tree_other, h)
        return tree_result

    # sort the empty binomial tree with a correct order.
    def sort_empty_tree(self, tree1, tree2, h):  # h is depth of input trees.
        tree_result = [tree1.pop(0)]  # place the root node.
        for i in range(1, h + 1):  # place nodes on level i.
            for x in range(0, comb(h, i - 1)):
                tree_result.append(tree2.pop(0))
            for y in range(0, comb(h, i)):
                tree_result.append(tree1.pop(0))
        tree_result.append(tree2.pop(0))  # place the tail node.
        return tree_result


class BinomialTree:
    def __init__(self, array):
        self.array = array
        self.len = len(array)
        self.depth = int(log(self.len, 2))  # make sure the depth is an integer.
        self.root = Node()  # create a root node.
        self.nodes = self.root.create_empty_BinomialTree(self.depth)
        self.tail = self.nodes[-1]

        # assign values from array to nodes.
        i = 0
        for n in array:
            self.nodes[i].value = n
            i += 1

    def HeapOrder(self):
        for node in self.nodes[::-1]:
            if node.parent is None or node.parent.value is None:
                continue

            while node.value < node.parent.value:
                if node.value is None:
                    continue  # no need to swap if the child is empty.

                # swap if the child is smaller than the parent,
                # or the parent is empty.
                node.parent.value, node.value = node.value, node.parent.value

                # let the current parent node be the child node for the next.
                node = node.parent

                if node.parent is None:
                    break

                if node.parent.value is None:
                    break

        # assign values with correct order in the array.
        i = 0
        for node in self.nodes:
            self.array[i] = node.value
            i += 1
        return

    def merge_empty_nodes(self, other_tree):
        # merge only when the depths are the same.
        if self.depth != other_tree.depth:
            print("The depths of the trees do not match")
            return

        # connect the root nodes
        self.root.connect(other_tree.root)

        # relocate the nodes into the correct order.
        nodes_result = []
        for h in range(0, self.depth + 1):
            if h == self.depth + 1:
                pass
            for x in range(0, comb(self.depth, h)):
                if h == 0:
                    pass
                for y in range(0, comb(self.depth, h - 1)):
                    nodes_result.append(other_tree.nodes.pop(0))
                nodes_result.append(self.nodes.pop(0))
        self.nodes = nodes_result
        return

    def update(self):
        # update depth and length based on the node structure.
        self.depth = 0
        cursor = self.root
        while cursor.child != []:
            self.depth += 1
            cursor = cursor.child[-1]
        self.len = 2**self.depth
        return

    def merge(self, other_tree):
        # make sure the merged trees have the same depth.
        if self.depth != other_tree.depth:
            print(
                "Merge is not performed "
                + "because the depth of the trees do not match"
            )
            return self

        # determine which tree has a smaller root node.
        if self.root.value <= other_tree.root.value:
            tree_small = self
            tree_big = other_tree
        else:
            tree_small = other_tree
            tree_big = self

        # make connection between the root nodes.
        tree_small.root.child.append(tree_big.root)
        tree_big.root.parent = tree_small.root

        # update the tail node.
        tree_small.tail = tree_big.tail

        # update the length and depth of the tree.
        tree_small.update()

        # restore the heap order.
        tree_small.HeapOrder()
        return tree_small

    def deleteMin(self):
        # swap the values of the root node and thet tail node.
        self.root.value, self.tail.value = self.tail.value, self.root.value

        # remove the value of the tail node
        self.tail.value = None

        # restore heap order
        self.HeapOrder()
        return

    def insert(self, n):
        # insert to the value to the tail node if its value is None.
        if self.tail.value is None:
            self.tail.value = n

            # restore heap order
            self.HeapOrder()
        else:
            print("The tail node is not empty.")
        return


if __name__ == "__main__":
    input = [100, 7, 30, 1]
    a = Node()
    tree = a.create_empty_BinomialTree(3)
    i = 0
    for node in tree:
        print("node number ", i, " is : ", node, node.parent, node.child)
        i += 1

    tree2 = BinomialTree(input)
    print(tree2.array)
    tree2.HeapOrder()
    print(tree2.array)
    tree2.HeapOrder()
    print(tree2.array)
    tree2.HeapOrder()
    print(tree2.array)

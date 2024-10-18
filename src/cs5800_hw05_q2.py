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
        self.depth = int(log(self.len, 2))  # make sure the depth is integer.
        self.root = Node()  # create a root node.
        self.nodes = self.root.create_empty_BinomialTree(self.depth)
        self.tail = self.nodes[-1]

        # assign values from array to nodes.
        i = 0
        for n in array:
            self.nodes[i].value = n
            i += 1

    def HeapOrder(self):
        """
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
        """
        # assign values with correct order in the array.
        i = 0
        for node in self.nodes:
            self.array[i] = node.value
            i += 1
        return

        # sort the empty binomial tree with a correct order.

    def merge(self, other_tree):
        # if other_tree has smaller root, swap self and other_tree.
        if other_tree.root.value < self.root.value:
            self, other_tree = other_tree, self

        # connect the nodes.
        self.root.connect(other_tree.root)

        # place nodes into corret order.
        nodes_result = [self.nodes.pop(0)]  # place the root node.
        for i in range(1, self.depth + 1):  # place nodes on level i.
            for x in range(0, comb(self.depth, i - 1)):
                nodes_result.append(other_tree.nodes.pop(0))
            for y in range(0, comb(self.depth, i)):
                nodes_result.append(self.nodes.pop(0))
        nodes_result.append(other_tree.nodes.pop(0))  # place the tail node.

        # update attrs of self after the merge.
        self.nodes = nodes_result
        self.root = nodes_result[0]
        self.tail = nodes_result[-1]
        self.depth = self.depth + 1
        self.len = 2**self.depth

        # initialize the array with correct length.
        self.array = self.array + other_tree.array

        # restore heap order.
        self.HeapOrder()
        return

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
    input_2 = [345, 1346, 34551, 25477]
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

    tree_1 = BinomialTree(input)
    tree_2 = BinomialTree(input_2)
    print(tree_1.array, "tree 1")
    tree_1.deleteMin()
    print(tree_1.array)
    tree_1.insert(0)
    print(tree_1.array, tree_2.array)
    tree_1.merge(tree_2)
    print(tree_1.array)

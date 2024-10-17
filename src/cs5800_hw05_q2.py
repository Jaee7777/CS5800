from math import log, factorial


# function for the number of combinations.
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
                print(
                    i,
                    i + len_level // 2,
                )
                self.nodes[i].connect(self.nodes[i + len_level // 2])
            len_level = len_level // 2

        # assign a root node and a tail node.
        self.root = self.nodes[0]
        self.tail = self.nodes[-1]

        # assign values to the nodes.
        i = 0
        for n in self.array:
            self.nodes[i].value = n
            i += 1
        print(self.root.child[2].value, "child")

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

    def HeapOrder(self):
        # if the depth is zero, there is only one node, so no need to run HeapOrder.
        if self.depth == 0:
            return

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


"""
        # initialize for the root node.
        parent_node = self.root
        child_values = [
            child.value for child in self.root.child if child.value is not None
        ]

        # stop HeapOrder if the root does not have any numerical child values.
        if child_values == []:
            return
        child_min_value = min(child_values)

        # compare the values of the parent node and the minimum child node.
        while parent_node.value > child_min_value:
            print(len(self.root.child))
            print(child_values)
            print(parent_node.value, child_min_value, "heaporder: parend, child min")
            # find the index for where the minimum child value exists.
            i = 0
            while parent_node.child[i].value != child_min_value:
                i += 1

            # perform parent-child value swap
            parent_node.value, parent_node.child[i].value = (
                parent_node.child[i].value,
                parent_node.value,
            )

            # let the minimum value child node to be the next parent node.
            parent_node = parent_node.child[i]
            child_values = [child.value for child in parent_node.child]

            # break the loop if there is no more numerical values to compare.
            if child_values == []:
                break
            child_min_value = min(child_values)

        # assign values with correct order in the array.
        i = 0
        for node in self.nodes:
            self.array[i] = node.value
            i += 1
        return
"""

if __name__ == "__main__":
    input = [7, 8, 12, 166, 1, 34, 15]
    input2 = [1, 100, 3, 4, 2, 1234, 566]
    a = BinomialTree(input)
    b = BinomialTree(input2)
    print(a.array, b.array)
    print([node.value for node in a.nodes])

    a.insert(11)
    print([node.value for node in a.nodes])
    print(a.array)
    print(a.tail.value, "insert in a")

    print(a.root, a.tail, a.root.value, a.tail.value, "root and tail of a before merge")

    print(a.depth, a.len, "depth and length of abefore merge")
    dd = a.merge(b)
    print(dd.array)
    print(a.root.value, a.tail.value, "root and tail of a after merge")

    print(dd.root.value, dd.tail.value, "root and tail of a.merge assigned to dd")
    print(dd.root.child)

    print(dd.root, dd.root.child, "dd root child")
    dd.deleteMin()
    print(dd.root.value, dd.tail.value, "root, tail after delete min")

    print(dd.tail.value, "tail value")

    dd.insert(123)
    print(dd.tail.value, "tail after insert 123")

    print(dd.array)

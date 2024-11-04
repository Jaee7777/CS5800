from math import log, factorial
from copy import deepcopy


# function for the number of combinations.
def comb(n, h):
    return factorial(n) // (factorial(h) * factorial(n - h))


class Node:
    # initialize a node. default value is float("inf").
    def __init__(self, value=float("inf")):
        self.parent = None
        self.child = []
        self.value = value

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

    def update(self):
        # update the array form using the nodes.
        i = 0
        for node in self.nodes:
            self.array[i] = node.value
            i += 1
        return

    def merge(self, other_tree):
        # if other_tree has smaller root, call merge on other_tree.
        if other_tree.root.value < self.root.value:
            other_tree.merge(self)
            return False

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

        # assign values with correct order in the array.
        self.update()
        return

    def deleteMin(self):
        # min element to return.
        result_min_value = self.root.value

        # remove the value of the tail node, and mark empty as float("inf").
        i = -1
        while self.nodes[i].value == float("inf"):
            i -= 1

        # swap the values of the root node and thet tail node.
        self.root.value, self.nodes[i].value = self.nodes[i].value, self.root.value
        self.nodes[i].value = float("inf")
        self.tail = self.nodes[i]

        # restore heap order, top to bottom.
        cursor = self.root
        # find minimum value among the child nodes.
        min_child_value = min([x.value for x in cursor.child])
        while cursor.child != [] and cursor.value > min_child_value:
            # find the node that has the minimum value.
            min_child = cursor.child[0]
            i = 0
            while min_child.value != min_child_value and i < len(cursor.child) - 1:
                i += 1
                min_child = cursor.child[i]
            # swap cursor value with the minimum child node value.
            cursor.value, min_child.value = min_child.value, cursor.value
            # set cursor to be the swapped child node.
            cursor = min_child
            if cursor.child != []:
                min_child_value = min([x.value for x in cursor.child])

        # update the array form.
        self.update()
        return result_min_value

    def insert(self, n):
        # insert to the value to the tail node if its value is float("inf").
        if self.tail.value == float("inf"):
            self.tail.value = n

            # restore heap order, bottom to top.
            cursor = self.tail
            while cursor.value < cursor.parent.value:
                cursor.value, cursor.parent.value = cursor.parent.value, cursor.value
                cursor = cursor.parent

                # breaek the while loop if the cursor reaches the root node.
                if cursor == self.root:
                    break

            # update the array form.
            self.update()
        else:
            print("The tail node is not empty.")
        return


def merge(a, b):
    Tree_a = BinomialTree(a)
    Tree_b = BinomialTree(b)
    check = Tree_a.merge(Tree_b)
    if check is False:
        return Tree_b.array
    else:
        return Tree_a.array


def deleteMin(a):
    Tree_a = BinomialTree(a)
    return Tree_a.deleteMin()


def insert(a):
    Tree_a = BinomialTree(a)
    Tree_a.insert()
    return Tree_a.array


if __name__ == "__main__":
    ### Test merge
    assert merge([1, 3], [0, 2]) == [0, 1, 2, 3]
    print(merge([1, 3], [0, 2]))
    assert merge([0, 2], [1, 3]) == [0, 1, 2, 3]
    print(merge([0, 2], [1, 3]))
    assert merge([0], [1]) == [0, 1]
    print(merge([0], [1]))
    assert merge([1], [0]) == [0, 1]
    print(merge([1], [0]))
    assert merge([7, 12, 8, 13], [3, 5, 4, 9]) == [3, 7, 5, 4, 12, 8, 9, 13]
    print(merge([7, 12, 8, 13], [3, 5, 4, 9]))
    assert merge([3, 5, 4, 9], [7, 12, 8, 13]) == [3, 7, 5, 4, 12, 8, 9, 13]
    print(merge([3, 5, 4, 9], [7, 12, 8, 13]))

    ### Test deleteMin
    arr = [3, 5, 4, 9]
    assert deleteMin(arr) == 3
    assert arr == [4, 5, 9, float("inf")]
    print(arr)
    assert deleteMin(arr) == 4
    print(arr)
    assert arr == [5, 9, float("inf"), float("inf")]
    assert deleteMin(arr) == 5
    assert arr == [9, float("inf"), float("inf"), float("inf")]
    arr = [3, 7, 5, 4, 12, 8, 9, 13]
    assert deleteMin(arr) == 3
    assert arr == [4, 7, 5, 13, 12, 8, 9, float("inf")]
    assert deleteMin(arr) == 4
    assert arr == [5, 7, 9, 13, 12, 8, float("inf"), float("inf")]
    assert deleteMin(arr) == 5
    assert arr == [7, 8, 9, 13, 12, float("inf"), float("inf"), float("inf")]

    arr = [3, 4, 5, 7, 12, 8, 9, 13]
    assert deleteMin(arr) == 3
    assert arr == [4, 8, 5, 7, 12, 13, 9, float("inf")]
    assert deleteMin(arr) == 4
    assert arr == [5, 8, 9, 7, 12, 13, float("inf"), float("inf")]
    assert deleteMin(arr) == 5
    assert arr == [7, 8, 9, 13, 12, float("inf"), float("inf"), float("inf")]

    arr = merge([3, 4, 5, 7, 12, 8, 9, 13], [5, 6, 7, 9, 14, 10, 11, 15])
    assert deleteMin(arr) == 3
    assert arr == [4, 5, 8, 5, 7, 6, 7, 9, 12, 15, 9, 14, 10, 11, 13, float("inf")]
    assert deleteMin(arr) == 4
    print(arr)
    assert arr == [
        5,
        6,
        8,
        5,
        7,
        10,
        7,
        9,
        12,
        15,
        9,
        14,
        13,
        11,
        float("inf"),
        float("inf"),
    ]
    assert deleteMin(arr) == 5
    assert arr == [
        5,
        6,
        8,
        9,
        7,
        10,
        7,
        9,
        12,
        15,
        11,
        14,
        13,
        float("inf"),
        float("inf"),
        float("inf"),
    ]

    arr = merge([3, 4, 5, 7, 5, 8, 9, 6], [5, 6, 7, 9, 14, 10, 11, 15])
    assert deleteMin(arr) == 3
    assert arr == [4, 5, 5, 5, 7, 6, 7, 9, 6, 8, 9, 14, 10, 11, 15, float("inf")]
    assert deleteMin(arr) == 4
    assert arr == [
        5,
        6,
        5,
        5,
        7,
        10,
        7,
        9,
        6,
        8,
        9,
        14,
        15,
        11,
        float("inf"),
        float("inf"),
    ]
    assert deleteMin(arr) == 5
    assert arr == [
        5,
        6,
        6,
        5,
        7,
        10,
        7,
        9,
        11,
        8,
        9,
        14,
        15,
        float("inf"),
        float("inf"),
        float("inf"),
    ]

    ### Test insert
    arr = merge([3, 4, 5, 7, 5, 8, 9, 6], [5, 6, 7, 9, 14, 10, 11, 15])
    deleteMin(arr)
    deleteMin(arr)
    deleteMin(arr)
    insert(arr, 11)
    assert arr == [
        5,
        6,
        6,
        5,
        7,
        10,
        7,
        9,
        11,
        8,
        9,
        14,
        15,
        11,
        float("inf"),
        float("inf"),
    ]
    insert(arr, 15)
    assert arr == [5, 6, 6, 5, 7, 10, 7, 9, 11, 8, 9, 14, 15, 11, 15, float("inf")]
    insert(arr, 7)
    assert arr == [5, 6, 6, 5, 7, 7, 7, 9, 11, 8, 9, 10, 15, 11, 15, 14]

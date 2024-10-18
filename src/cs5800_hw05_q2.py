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
            print("The merge is done on the input tree instead")
            return

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

        # swap the values of the root node and thet tail node.
        self.root.value, self.tail.value = self.tail.value, self.root.value

        # remove the value of the tail node, and mark empty as None.
        self.tail.value = None

        # restore heap order, top to bottom.
        cursor = self.root
        # find minimum value among the child nodes.
        min_child_value = min([x.value for x in cursor.child])
        while cursor.child != [] and cursor.value > min_child_value:
            # find the node that has the minimum value.
            min_child = cursor.child[0]
            i = 0
            while min_child.value != min_child_value and i < len(cursor.child):
                min_child = cursor.child[i]
                i += 1
            # swap cursor value with the minimum child node value.
            cursor.value, min_child.value = min_child.value, cursor.value
            # set cursor to be the swapped child node.
            cursor = min_child

        # update the array form.
        self.update()
        return result_min_value

    def insert(self, n):
        # insert to the value to the tail node if its value is None.
        if self.tail.value is None:
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


if __name__ == "__main__":
    input_1 = [7, 12, 8, 13]
    input_2 = [3, 5, 4, 9]
    p = BinomialTree(input_1)
    q = BinomialTree(input_2)
    print("p is : ", p.array)
    print("q is : ", q.array)

    deleted_min = p.deleteMin()
    print("p after deleteMin(p) is : ", p.array)
    print("deleted min value from p is : ", deleted_min)

    p.insert(6)
    print("p after insert(p,6) is : ", p.array)

    print("p before merge(p,q) is : ", p.array)
    print("q before merge(p,q) is : ", q.array)
    p.merge(q)
    # q.merge(p)
    print("p after merge(p,q) is : ", p.array)
    print("q after merge(p,q) is : ", q.array)

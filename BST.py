"""
Binary search tree API

"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None


class BST:
    def __init__(self):
        self.root = None
        self.leftChild = None
        self.rightChild = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    """
    Search for key
    """
    def search(self, currentNodeKey, keyBeingSearched):
        if currentNodeKey.leftChild is None and currentNodeKey.rightChild is None:
            return "Key does not exist in the tree"
        else:
            if currentNodeKey.key == keyBeingSearched:
                return currentNodeKey.value
            elif currentNodeKey.key > keyBeingSearched:
                return BST.search(self, currentNodeKey.rightChild, keyBeingSearched)
            else:
                return BST.search(self, currentNodeKey.leftChild, keyBeingSearched)

    """
    Node is the value to be inserted in the BST
    """

    def insert(self, root, NodeValue):
        if root is None:
            self.root = Node(NodeValue)
            self.size += 1
        elif NodeValue > root.value:
            if root.leftChild is None:
                root.leftChild = Node(NodeValue)
                self.size += 1
            return BST.insert(self, root.rightChild, NodeValue)
        else:
            if root.rightChild is None:
                root.rightChild = Node(NodeValue)
                self.size += 1
            return BST.insert(self, root.leftChild, NodeValue)

    def delete(self, value):
        # search value
        # delete
        # move up right child of the node that just got removed
        # restore tree order
        pass

    def replace(self, value, newValue):
        # search for value
        # replace with new value
        # restore tree order
        pass

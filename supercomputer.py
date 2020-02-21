class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray(object):
    def __init__(self,arr):
        self.arr = arr
        #initialize data structure

    def createTree(self, arr, l, r):
        #base case
        if l > r:
            return None
        #leaf case
        if l == r:
            n = Node(l,r)
            n.total = arr[l]
            return n

        #recursive case
        mid = (l+r) //2
        root = Node(l,r)
        root.left = self.createTree(arr, l, mid)
        root.right = self.createTree(arr, mid+1, r)

        root.total = root.left.total + root.right.total
        return root

        root = createTree(self.arr, 0, len(self.arr)-1)


    def updateVal(root, i, val):

            #Base case. The actual value will be updated in a leaf.
            #The total is then propogated upwards
            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end) // 2

            #If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)

            #Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)

            #Propogate the changes after recursive call returns
                root.total = root.left.total + root.right.total

                return root.total

            return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def rangeSum(root, i, j):

            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) // 2

            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)

            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)

            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)

        return rangeSum(self.root, i, j)


if __name__ == "__main__":
    N, K = [int(x) for x in input().split()]
    arr= [0]*N #create the string
    numArray = NumArray(arr) #initialize data structure
    right = len(arr)-1
    numArray.createTree(arr, 0, right) # createtheTree

    for i in range(K):
        inst = input().split() #take in instruction
        if inst[0] == "F":
            if arr[inst[1]] == 0:
                numArray.updateVal(inst[1], 1)
            else:
                numArray.updateVal(inst[1], 0)
        if inst[0] == "C":
            num_1 = numArray.sumRange(inst[1],inst[2])
            print(num_1)

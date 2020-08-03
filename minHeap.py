"""
Implementation of a maximum priority queue
in python using complete binary tree
"""


class minHeap:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    def isLeafIndex(self, index):
        if (self.currentSize // 2) <= index <= self.currentSize:
            return True
        return False

    def restoreHeapOrder(self, index):
        currentIndex = index
        leftChild = (2*currentIndex) + 1
        rightChild = (2*currentIndex) + 2

        while not self.isLeafIndex(currentIndex):
            if self.heapList[currentIndex] > self.heapList[leftChild] or self.heapList[currentIndex] > self.heapList[rightChild]:
                if self.heapList[leftChild] < self.heapList[rightChild]:
                    self.heapList[currentIndex], self.heapList[leftChild] = self.heapList[leftChild], self.heapList[currentIndex]
                    currentIndex = leftChild
                else:
                    self.heapList[rightChild], self.heapList[currentIndex] = self.heapList[currentIndex], self.heapList[rightChild]
                    currentIndex = rightChild
                rightChild = (2*currentIndex) + 2
                leftChild = (2 * currentIndex) + 1

    def insert(self, key):
        if self.currentSize == 0:
            self.heapList.append(key)
            self.currentSize += 1
        else:
            self.heapList.append(key)
            self.currentSize += 1
            index = self.currentSize-1
            parentIndex = int((index - 1) / 2)
            while self.heapList[index] < self.heapList[parentIndex]:
                self.heapList[index], self.heapList[parentIndex] = self.heapList[parentIndex], self.heapList[index]
                index = parentIndex

    def deleteMin(self):
        temp = self.heapList[0]
        self.heapList[0] = self.heapList[-1]
        self.heapList[-1] = temp
        delVertex = self.heapList.pop()
        self.currentSize -= 1
        self.restoreHeapOrder(0)
        return delVertex

    def toString(self):
        return self.heapList


if __name__ == "__main__":
    array = [14, 41, 31, 16, 51, 100]
    heap = minHeap()
    for i in range(len(array)):
        heap.insert(array[i])
    print(heap.toString())

    heap.deleteMin()
    print(heap.toString())

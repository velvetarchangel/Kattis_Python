"""
Implement different types of sorts in Python

"""
import math

def insertionSort(array):
    i = 1
    while i < len(array):
        key = array[i]
        j = i - 1
        while j > 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = key
        i += 1
    return array


def selectionSort(array):
    minIndex = 0

    while minIndex < len(array):
        currentIndex = minIndex
        while currentIndex < len(array):
            if array[currentIndex] < array[minIndex]:
                array[minIndex], array[currentIndex] = array[currentIndex], array[minIndex]
            currentIndex += 1
        minIndex += 1
    return array


def merge(A, B, list):
    """
    helper function for mergeSort
    :param A: array from the first index to mid
    :param B: array from mid + 1 to last index
    :return: merged and sorted array
    """

    indexA = 0
    indexB = 0
    indexC = 0

    while indexA < len(A) and indexB < len(B):
        if A[indexA] <= B[indexB]:
            list[indexC] = A[indexA]
            indexA += 1
            indexC += 1
        else:
            list[indexC] = B[indexB]
            indexB += 1
            indexC += 1

    while indexA < len(A):
        list[indexC] = A[indexA]
        indexC += 1
        indexA += 1

    while indexB < len(B):
        list[indexC] = B[indexB]
        indexC += 1
        indexB += 1
    return list


def mergeSort(array):
    if len(array) < 2:
        return array
    mid = math.floor(len(array)/2)
    A = array[0:mid]
    B = array[mid:]
    mergeSort(A)
    mergeSort(B)
    return merge(A, B, array)


def heapSort(array):
    return


def quickSort(array):
    return


if __name__ == "__main__":
    test_array = [6, 9, 17, 3, 81, 4, 5]
    a = mergeSort(test_array)
    print(a)




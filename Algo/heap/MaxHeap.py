# pow(2, h+1)-1 is size of the tree
# log n is the height of the tree.

# o(n log n) time and space complexity.


def heapify(arr):
    n = len(arr)
    # indices floor(n/2+1) -> n are leave nodes
    # in any complete/almost complete binary tree.
    # iterate through all parents from last parent to first.
    for index in range(n/2, -1, -1):
        shiftDown(arr, index)


def shiftDown(arr, index):
    left = 2*index
    largest = index
    if left < len(arr) and arr[left] > arr[index]:
        largest = left

    if left+1 < len(arr) and arr[left+1] > arr[index]:
        largest = left+1

    if largest != index:
        swap(arr, largest, index)
        shiftDown(arr, largest)
    return


def swap(arr, frm, to):
    arr[frm], arr[to] = arr[to], arr[frm]
    return


a = [1, 2, 3, 4, 5]
heapify(a)
print(a)

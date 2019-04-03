

def create_heap(arr, size, index):
    largest_index = index
    left_index = (2 * index) + 1
    right_index = (2 * index) + 2
    
    # swap root node with child node if child node is larger
    if left_index < size and arr[left_index] > arr[largest_index]:
        largest_index = left_index
    if right_index < size and arr[right_index] > arr[largest_index]:
        largest_index = right_index
    
    if largest_index != index:
        arr[index], arr[largest_index] = arr[largest_index], arr[index]

        create_heap(arr, size, largest_index)

def heap_sort(arr, size):
    # create max heap from rightmost (last non-leaf) node
    for index in range(size/2 - 1, -1, -1):
        create_heap(arr, size, index)
    
    # swap root node with outermost index and rebuild the max heap on resulting sub-array and repeat
    for index in range(size-1, -1, -1):
        arr[index], arr[0] = arr[0], arr[index]
        create_heap(arr, index, 0)
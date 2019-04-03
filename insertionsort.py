
def insertion_sort(arr): 
    for i, val in enumerate(arr):
        if i == 0:
            continue

        j = i - 1
        while j >= 0 and val < arr[j]: 
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = val 
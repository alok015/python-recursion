def quickSort(arr, start, end):
    if start >= end:
        return
    pivot_index = partition(arr, start, end)
    quickSort(arr, start, pivot_index - 1)
    quickSort(arr, pivot_index + 1, end)


def partition(arr, start, end):
    pivot = arr[start]
    # find number of elements smaller than pivot
    c = 0
    for i in range(start, end + 1):
        if arr[i] < pivot:
            c += 1

    arr[start + c], arr[start] = arr[start], arr[start + c]

    pivot_index = start + c

    i = start
    j = end

    while i < j:
        if arr[i] < pivot:
            i += 1
        elif arr[j] > pivot:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return pivot_index

arr = [6,10,9,8,7,1,3,5,4,2]
quickSort(arr,0,len(arr)-1)
print(arr)

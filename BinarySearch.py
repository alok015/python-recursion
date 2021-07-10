def BinarySearch(arr,x,si,end):

    if si>end:
        return -1
    mid = (si+end)//2
    if arr[mid]==x:
        return mid
    elif arr[mid]>x:
        return BinarySearch(arr, x, si, mid-1)
    else:
        return BinarySearch(arr, x,mid+1, end)

arr = [1,3,5,7,9,11,13,15,16,17]
si = 0
end = len(arr)-1
print(BinarySearch(arr, 3, si, end))
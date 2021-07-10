def sumArray(arr):
    n = len(arr)
    if (n==1):
        return arr[0]
    smallAns = sumArray(arr[:n-1])
    return smallAns + arr[n-1]

print(sumArray([1,2,3,4,5]))
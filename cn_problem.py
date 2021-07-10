def sumArray(arr):
    if len(arr) == 0:
        return 0
    else:
        smaller_array = arr[1:]
        return arr[0] + sumArray(smaller_array)
        # Please add your code here


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
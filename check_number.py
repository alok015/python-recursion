def checkNumber(arr, x):
    if len(arr)==0:
        return False
    if arr[0] ==x:
        return True
    else:
        smaller_array = arr[1:]
        return checkNumber(smaller_array,x)

arr = [1,2,3,4,5,6]
x = 3
print(checkNumber(arr,x))

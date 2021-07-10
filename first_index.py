# def firstIndex(arr, x):
#     if len(arr)==0:
#         return -1
#     if arr[0]==x:
#         return 0
#     smaller_list = arr[1:]
#     smaller_list_output = firstIndex(smaller_list,x)
#
#     if smaller_list_output == -1:
#         return -1
#     else:
#         return  1+smaller_list_output

def firstIndex(arr, x, si=0):
    if len(arr) == 0:
        return -1
    if arr[si] == x:
        return si
    smaller_list_output = firstIndex(arr, x, si + 1)
    return smaller_list_output
    # Please add your code he
arr = [1,3,5,7,9,7,11]
x = 7
print(firstIndex(arr,x,si=0))

def firstIndex(arr, x, si=0):
    if len(arr) == 0:
        return -1
    if arr[si] == x:
        return si
    smaller_list_output = firstIndex(arr, x, si + 1)
    return smaller_list_output
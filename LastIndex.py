# def lastIndex(arr, x, si):
#     if si== -1:
#         return -1
#     if arr[si] == x:
#         return si
#     smaller_list_output = lastIndex(arr, x, si - 1)
#     return smaller_list_output
# arr = [1,3,5,7,9,7,11]
# x = 13
# si = len(arr)-1
# print(lastIndex(arr,x,si))
def lastIndex(arr, x, si):
    if si == -1:
        return -1
    if arr[si] == x:
        return si
    smaller_list_output = lastIndex(arr, x, si - 1)
    return smaller_list_output
n = int(input())
arr = list(map(int,input.split(' ')[:n]))
x=int(input())
si = len(arr)-1
print(lastIndex(arr,x,si))
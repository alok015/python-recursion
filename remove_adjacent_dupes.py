def removeCD(str):
    l = len(str)
    if l==0 or l ==1:
        return str
    if(str[0]==str[1]):
        return removeCD(str[1:])
    else:
        return str[0] + removeCD(str[1:])

string = 'aaaaabbbcccc'
print(removeCD(string))
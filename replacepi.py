def replacePi(string):
    print(string)
    if len(string)==1 or len(string)==0:
        return string
    print(string)
    if string[0]=='p' and string[1]=='i':
        print(string)
        smallOutput = replacePi(string[2:])
        print(string)
        return '3.14' + smallOutput

    else:
        print(string)
        smallOutput = replacePi(string[1:])
        print(string)
        return string[0]+smallOutput

b = 'ppiwecdpi'
print(replacePi(b))
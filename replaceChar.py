def replaceChar(s,a,b):
    print(s,a,b)
    if len(s)==0:
        return s
    smallOutput = replaceChar(s[1:],a,b)
    m = s
    print(m)
    if s[0]==a:
        return b + smallOutput
    else:
        return s[0]+smallOutput

str=replaceChar('daaxbcmd','a','x')
print(str)


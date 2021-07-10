def removeX(string):
    if len(string) == 0:
        return string
    smallerOutput = removeX(string[1:])
    if string[0] == 'x':
        return '' + smallerOutput
    else:
        return string[0] + smallerOutput


# Main
string = 'abbxxxxxcdb'
print(removeX(string))
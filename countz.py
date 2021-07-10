def countz(n):
    if n<10:
        if n==0:
            return 1
        else:
            return 0
    print('function is called with', n)
    small = countz(n//10)
    print("n is ",n)
    print('Value of small is ',small)
    if n%10 ==0:
        print('n is 1st condition and it is  ',n, 'value of small is  ',small)

        return small + 1
    else:
        print('n is 2st condition and it is  ', n, 'and value of small is  ', small)

        return small

print(countz(400050))

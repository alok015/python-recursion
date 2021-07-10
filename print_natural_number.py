def print_1_to_n(n):
    if n==0:
        return
    print('Called for before',n)
    print_1_to_n(n-1)
    print('called after ',n)

print_1_to_n(5)

def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
def sum(n):
    if n ==0:
        return 0
    else:
        return n + sum(n-1)
factorial = fact(10)
sum_n = sum(10)
print(factorial)
print(sum_n)


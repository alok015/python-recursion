def sum(n):
    if n==0:
        return 1
    geo_sum = 1/pow(2,n) + sum(n-1)
    return geo_sum

n=int(input())
print("%.5f" %sum(n))




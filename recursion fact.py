def num(n):
    if n==1:
        return 1
    else:
        return n+num(n-1)
n=int(input("enter num"))
print(num(n))

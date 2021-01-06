n=int(input("enter n="))
a=-1
b=1
if(n==1 and n==0):
    print(0,1)
while n>=2:
    print(a+b)
    b=a+b
    a=b-a
    n-=1

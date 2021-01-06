x=int(input("enter the 1st value"))
y=int(input("enter the 2nd value"))
count=5
if x>y:
    n=x
    print("x is greater")
else:
    n=y
    print("y is greater")
while (count>=1):
    if((n%x==0) and (n%y==0)):
        print(n)
        break
    n+=1
print("the lcm of {0} and {1} is {2}".format(x,y,n))
    

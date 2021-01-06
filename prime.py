n=int(input("enter your number:"))
div =2
while div<n:
    if n%div==0:
        print("not prime")
        break
    div+=1
else:
    print("prime")

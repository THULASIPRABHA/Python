no = int(input("Enter no="))
a=no

sum=0
while no>0:
    rem=no%10
    sum=(sum) + (rem*rem*rem)
    no=no//10
if a==sum:
    print(a," is a armstrong number")
else:
    print(a,"is not a armstrong number")

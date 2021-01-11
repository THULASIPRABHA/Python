sum=0
def sumOfDigits(num):
    global sum
    if num>0:
        rem = num%10
        sum=sum*10+rem
        num = num//10
        sumOfDigits(num)
    return sum
    
number=int(input("enter the number="))
rev=sumOfDigits(number)
print("reverse number is",rev)

num=int(input("enter binary number-"))
#count= " "
i,s=1,0
while num >0: 
    rem=(num %2)
    s=s+(i*rem)
    #count=str(rem)+count
    #print(count)
    num=num/2
    i=i*10
   
else:
    print(binary)

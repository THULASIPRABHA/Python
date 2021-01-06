num=int(input("enter number-"))
count= " "
while num >0: 
    rem=(num %2)
    
    count=str(rem)+count
    #print(count)
    num=num//2
   
else:
    print(count)
  

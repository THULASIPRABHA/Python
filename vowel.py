name = input("What is your name? ")
length = len(name)
i =0
while i<length:
    if name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u':
        print(name[i])

    i=i+1 

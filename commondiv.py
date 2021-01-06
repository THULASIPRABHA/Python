
a = int(input(" Please Enter the First Value a: "))
b = int(input(" Please Enter the Second Value b: "))
i = 1
while(i <= a and i <= b):
    if(a % i == 0 and b % i == 0):
        common = i
        i = i + 1
        
print("common hcf of {0} and {1}={2}".format(a,b,common))

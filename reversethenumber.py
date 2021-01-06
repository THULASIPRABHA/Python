no = input("Enter no") #1234
reverse = ''
print(reverse)
i = len(no)-1
while i>=0:
	reverse = reverse + no[i] #'4321'
	i-=1
	
print(reverse)
if no==reverse:
    print("palindrome")
else:
    print("not palindrome")


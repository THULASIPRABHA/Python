def lcm(x, y):
    if y == 0:
        return x
    return x * y / lcm(x, y)

x=int(input("enter the 1st value="))
y=int(input("enter the 2nd value="))
print("The L.C.M. of", x,"and", y,"is", lcm(x,y))

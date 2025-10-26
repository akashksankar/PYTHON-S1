a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
c=float(input("enter the third number:"))
if a>=b and a>=c:
    print("this is biggest:",a)
elif b>=a and b>=c:
    print("this is biggest:",b)  
else:
    print("this is biggest:",c)      
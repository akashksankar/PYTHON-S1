class Rectangle:
def __init__(self,l,w):
self.__length=l
self.__width=w
def area(self):
return self.__length*self.__width
def __lt__(self, other):
if self.area()< other.area():
return True
else:
return False
l1=int(input("enter the length: "))
w1=int(input("enter the width: "))
r1=Rectangle(l1,w1)
l2=int(input("enter the length: "))
w2=int(input("enter the width: "))
r2=Rectangle(l2,w2)
if r1<r2:
print(f"area of r2 is greater:{r2.area()}")
else:
print(f"area of r1 is greater:{r1.area()}")

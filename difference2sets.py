a=input("enter colours:").split(",")
b=input("enter colours:").split(",")
r=[]
for color in a:
    if color not in b:
        r.append(color)
print(r)        
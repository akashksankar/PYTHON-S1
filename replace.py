s=input("Enter a string: ")
first=s[0]
rest=s[1:].replace(first,'$')
result=first+rest
print(result)

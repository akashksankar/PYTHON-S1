file=input("enter the file name:")
if "." in file:
 extension=file.split(".")[-1]
 print(extension)
else:
 print("no extension in this filename!") 
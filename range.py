current_year=int(input("enter ccurrent year:"))
final_year=int(input("enter final year:"))
print("Leap year between the range are:")
for year in range (current_year ,final_year+1):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)
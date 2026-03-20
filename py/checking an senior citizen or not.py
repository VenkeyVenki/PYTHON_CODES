import datetime
name=input("Enter Name:")
dy=int(input("Enter the year of birth:"))
d=datetime.date.today()
cy=d.year
age=cy-dy
if(age>=60):
    print("Person is Senior citizen.")
else:
    print("Person is not Senior citizen.")
#Program to check whether three given numbers can form the side of  a Triangle
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if(a+b<=c and b+c<=a and a+c<=b):
    print("It can not be an Triangle")
else:
    print("It is an Triangle")
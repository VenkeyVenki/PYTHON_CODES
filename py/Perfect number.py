n =int(input("Enter the number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("It's a Perfect number")
else:
    print("It's not a perfect number")
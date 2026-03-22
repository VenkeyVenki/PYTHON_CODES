n=int(input("Enter the length od Fibanaci Sequence:"))
a=0
b=1
i=0
sum=0
print("__FIBONACCI SERIES__")
while(i<n):
    print(a)
    sum=a+b
    a=b
    b=sum
    i+=1
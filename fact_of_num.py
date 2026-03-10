n=int(input("Enter a number:"))
fact=1
if n<0:
    print("Factirial does not exist for negative numbers")
elif n==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(f"The factorial of {n} is {fact}")
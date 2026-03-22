def fact(N):
    if N==0:
        return 1
    else:
        return N*fact(N-1)
N=int(input("Enter N:"))
R=int(input("Enter R:"))
print("Factorial of ",N,"is:",fact(N))
print("Factorial of ",R,"is:",fact(R))
bi=fact(N)/(fact(R)*fact(N-R))
print("Binomial Coefficinet",N,"&",R,"is:",bi)
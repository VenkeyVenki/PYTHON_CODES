import math
clcoding=math.pi
print(" Happy Pi Day!(March 14)")
print("Value of Pi:",round(clcoding,10))
print("\nPi Circle Pattern:\n")
for i in range(-10,11):
    for j in range(-10,11):
        if i*i+j*j<=100:
            print("*",end="")
        else:
            print(" ",end="")
    print()
print("\npi=3.141592635....")
print("Keep Coding with CLCODING")
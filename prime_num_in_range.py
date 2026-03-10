l=1 
u=10
print("Print number between",l,"and",u,"are:")
for n in range(l,u+1):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
            print(n)
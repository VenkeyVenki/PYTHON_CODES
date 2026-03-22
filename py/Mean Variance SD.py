#Read N numbers from the cansole and create a list to print mean,variance and standard deviation with suitable messages.
import math
n=int(input("Enter a range value to be read=>"))
list=[]
for i in range(n):
    list.append(int(input("Enter the values=>")))
mn=sum(list)/n
print("The mean of all List num=>%f"%mn)
vr=0
for i in list:
    vr=vr+(i-mn)**2
print("The Variance of all the List num=>%f"%(vr/n))
std=math.sqrt(vr)
print("The Standard Deviation of all the List num=>%f"%(std))
import statistics
n=int(input("Enter a range value to be read=>"))
list=[]
for i in range(n):
    list.append(int(input("Enter the values=>")))
print("The mean of all List num=>",statistics.mean(list))
print("The Variance of all the List num=>",statistics.pvariance(list))
print("The Standard Deviation of all the List num=>",statistics.pstdev(list))
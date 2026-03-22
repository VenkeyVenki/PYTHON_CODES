n = input("Enter the number: ")

for i in set(n):
    print("The frequency of digit", i, "=", n.count(i))
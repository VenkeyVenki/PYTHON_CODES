s = input("Enter the String:")
count = sum(1 for i in s if i in "aeiouAEIOU")
print(count)
def divexp(a,b):
    assert a>0,"a value cannot be 0"
    if b==0:
        raise Exception("b value cannot be 0")
    try:
        c=a/b
        return c
    except Exception as e:
        return e
a=int(input("Enter a value of a:"))
b=int(input("Enter a value of b:"))
print(divexp(a,b))
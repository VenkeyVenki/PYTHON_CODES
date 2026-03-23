class Complex:
    def __init__(self, tempReal, tempImaginary):
        self.real = tempReal
        self.img = tempImaginary
    def addcomplex(self, c1, c2):
        temp = Complex(0, 0)
        temp.real = c1.real + c2.real
        temp.img = c1.img + c2.img
        return temp
csum = Complex(0, 0)
n = int(input("Enter the number of complex numbers to be added: "))
for i in range(1, n + 1):
    print("Enter the real & img part of complex num %d:" % i, end=" ")
    c = input().split()
    c1 = Complex(int(c[0]), int(c[1]))
    csum = csum.addcomplex(csum, c1)
print("Sum of given complex number is = %d + i%d" % (csum.real, csum.img))
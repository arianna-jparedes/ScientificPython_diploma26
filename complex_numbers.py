#!/usr/bin/python3

class ComplexNumber():
    
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def add(self, other):
        r = self.real + other.real
        i = self.img + other.img
        return print(f"Sum: {r} + {i}i")

    def substract(self, other):
        r = self.real - other.real
        i = self.img - other.img
        return print(f"Substraction: {r} + {i}i")

    def multiply(self, other):
        r = self.real*other.real - self.img*other.img
        i = self.real*other.img + self.img*other.real
        return print(f"Multiplication: {r} + {i}i")

if __name__ == "__main__":
    z1 = ComplexNumber(2, 3)
    z2 = ComplexNumber(1, -4)

    z1.add(z2)
    z1.substract(z2)
    z1.multiply(z2)
    



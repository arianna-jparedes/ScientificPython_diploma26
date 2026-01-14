#!/usr/bin/env
import numpy as np

class Exercises:
    """
    This class have nine functions, corresponding to the exercises
    of the first lecture.
    """

    def __init__(self):
        pass

    def ex1(self, a, b, c):
        d = b**2 - 4*a*c
        if d > 0:
            x1 = (-b + np.sqrt(d))/(2*a)
            x2 = (-b - np.sqrt(d))/(2*a)
            return print("The two roots are: ", x1, "and", x2)
        elif d == 0:
            x = (-b + np.sqrt(d))/(2*a)
            return print("The root is: ", x)
        elif d < 0:
            return print("There are two distinct complex (imaginary) roots.")

    def ex2(self, n):
        a = []
        a.append(0)
        s = set()
        s.add(0)
        for i in range(1, n):
            x = a[i-1] - i
            if (x > 0 and x not in s):
                a.append(x)
                s.add(x)
            else:
                x = a[i-1] + i
                a.append(x)
                s.add(x)
        return a

    def ex3(self, l):
        l.sort()
        l.reverse()
        return l

    def ex4(self, l1, l2):
        l = [i for i in l1 if l2.count(i) >= 1]
        return l

    def ex5(self, n):
        l = [(i, n//i) for i in range(1, n+1) if n%i == 0]
        return l

    def ex6(self, n, step):
        l = list(range(0, n, step))
        return l

    def ex7(self, s):
        t = s.replace(" ", "").lower()
        return t == t[::-1]

    def ex8(self, s):
        t = s.replace(" ", "").lower()
        c = max(t, key=t.count)
        return(c, t.count(c))

    def ex9(self, n):
        primes = [True]*(n+1)
        for p in range(2, n+1):
            if primes[p]:
                for m in range(2*p, n+1, p):
                    primes[m] = False

        return [i for i in range(2, n+1) if primes[i]]
    

#!usr/bin/python3

from module_exercises import Exercises

def main():
    ex = Exercises()
    sol1 = ex.ex1(1, -3, -4)
    sol2 = ex.ex2(50)
    mylist=[1,-99,89,0,234,77,-748,11]
    sol3 = ex.ex3(mylist)
    l1 = [1, 3, 6, "cat", "dog"]
    l2 = [6, "dog", 8, 0]
    sol4 = ex.ex4(l1, l2)
    sol5 = ex.ex5(12)
    sol6 = ex.ex6(1000, 3)
    sol7 = ex.ex7("No lemon no melon")
    sol8 = ex.ex8("asakjbncoufhnklsnajd")
    sol9 = ex.ex9(30)

if __name__ == "__main__":
    main()

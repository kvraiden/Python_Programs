#Quadratic will require comlex math header import it first
import cmath
print('This is a simple program to find solution to quadratic problems.')
a = eval(input("Enter value of a : "))
b = eval(input("Enter value of b : "))
c = eval(input("Enter value of c : "))
d = b**2 - 4*a*c
sol1 = (-b-(cmath.sqrt(d))/2*a)
sol2 = (-b+(cmath.sqrt(d))/2*a)
print('Two solutions are there.')
print((sol1))
print((sol2))
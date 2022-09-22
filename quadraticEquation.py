import cmath

print("Enter the values of variable for the standard Quadratic equation ax^2 + bx + c = 0")
a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))
c = int(input("Enter Value of c: "))

sqrt_d = cmath.sqrt((b**2) - (4*a*c))

root1 = (-b - sqrt_d)/(2*a)
root2 = (-b + sqrt_d)/(2*a)

print('The real roots of the equation "{0}x^2 + {1}x + {2} = 0" are {3} and {4}\n'.format(a, b, c, root1.real, root2.real))

print('The imaginary roots of the equation "{0}x^2 + {1}x + {2} = 0" are {3} and {4}'.format(a, b, c, root1.imag, root2.imag))

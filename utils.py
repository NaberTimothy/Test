# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import sqrt

def fact(n):
    result = n
    if n ==0 or n ==1 :
        result = 1
    for i in range(n):
        if i != 0:
            result *= i
    return result


    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """

def roots(a, b, c):

    delta = b**2-(4*a*c)
    if delta < 0:
        return (0)
    if delta == 0:
        return (((-b)/(2*a)))
    if delta > 0:
        return ((-b-sqrt(delta))/(2*a),(-b+sqrt(delta))/(2*a))


    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    pass

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    pass

if __name__ == '__main__':
    print(fact(8))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))

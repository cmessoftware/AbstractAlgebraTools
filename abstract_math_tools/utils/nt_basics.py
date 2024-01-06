import math
from sympy import primepi

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n*factorial(n-1)


def gcd(a,b):
    return math.gcd(a,b)


def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def mod(a,n):
    return a%n

def exp_mod(a,b,n):
    return pow(a, b, n)

def mod_inverse(a, n):
    gcd, x, _ = xgcd(a, n)
    if gcd != 1:
        raise ValueError(f"The modular inverse does not exist for {a} modulo {n}")
    return x % n

def phi_function(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


def pi_function(n):
    return primepi(n)

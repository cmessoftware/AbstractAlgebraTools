import math
from sympy import primepi

def factorial(n):
    
    if n < 0:
        raise "n must be major than 0"
    
    if n == 0 or n == 1:
        return 1
    
    return n*factorial(n-1)


def has_bijections(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    mapping = {}
    
    for i in range(len(arr1)):
        if arr1[i] in mapping:
            if mapping[arr1[i]] != arr2[i]:
                return False
        else:
            mapping[arr1[i]] = arr2[i]
    
    return True

def has_unique_numbers(arr):
    return len(arr) == len(set(arr))

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
    amount = 0
    for k in range(1,n+1):
        if gcd(n,k) == 1:
            amount += 1
    return amount

def is_generator(a, n):
    if gcd(a, n) != 1:
        return False
    return pow(a, phi_function(n), n) == 1 and pow(a, n-1, n) == 1 
  
def pi_function(n):
    return primepi(n)

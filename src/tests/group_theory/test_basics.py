import pytest
from   src.utils.nt_basics import gcd, xgcd, mod, exp_mod, mod_inverse, phi_function, pi_function


# Test cases for gcd function
@pytest.mark.parametrize("a, b, expected", [
    (15, 25, 5),
    (35, 49, 7),
    (17, 23, 1),
    
])
def test_gcd(a, b, expected):
    assert gcd(a, b) == expected

# Test cases for xgcd function
@pytest.mark.parametrize("a, b, expected_gcd, expected_x, expected_y", [
    (15, 25, 5, 2, -1),
    (35, 49, 7, 3, -2),
    (17, 23, 1, -4, 3),
    
])
def test_xgcd(a, b, expected_gcd, expected_x, expected_y):
    gcd_result, x_result, y_result = xgcd(a, b)
    assert gcd_result == expected_gcd
    assert x_result == expected_x
    assert y_result == expected_y

# Test cases for mod function
@pytest.mark.parametrize("a, n, expected", [
    (10, 3, 1),
    (17, 5, 2),
    (1234, 23, 15),
    (233, 25, 8), 
    (25369, 25, 19), 
    (5269, 19, 6), 
    (63658, 212, 58), 
])
def test_mod(a, n, expected):
    assert mod(a, n) == expected

# Test cases for exp_mod function
@pytest.mark.parametrize("a, b, n, expected", [
    (2, 3, 5, 3),
    (3, 4, 7, 4),
    (23, 33, 4,3),
    (22223, 233, 224,143),
    (321313, 2321, 27,25),
    (19843, 33, 5,3),
    (2223, 2, 3,0),
    (33, 9, 24,9),
    (345, 23, 22,9),
    (100, 2, 2,0),
    (213, 3, 14,13)
])
def test_exp_mod(a, b, n, expected):
    assert exp_mod(a, b, n) == expected

# Test cases for mod_inverse function
@pytest.mark.parametrize("a, n, expected", [
    (3, 7, 5),
    (5, 11, 9),
    
])
def test_mod_inverse(a, n, expected):
    assert mod_inverse(a, n) == expected

# Test cases for phi_function function
@pytest.mark.parametrize("n, expected", [
    (10, 4),
    (15, 8),
])
def test_phi_function(n, expected):
    assert phi_function(n) == expected

# Test cases for pi_function function
@pytest.mark.parametrize("n, expected", [
    (10, 4),
    (15, 6),
    
])
def test_pi_function(n, expected):
    assert pi_function(n) == expected

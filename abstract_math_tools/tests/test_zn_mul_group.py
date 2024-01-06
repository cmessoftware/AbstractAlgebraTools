import pytest
from abstract_math_tools.zn_mul_group import zn_mul_group

n = 4
  
@pytest.fixture
def zn():
    return zn_mul_group(n)
    

def test_is_isomorphic(zn):
    assert zn.is_isomorphic('H') == True        

# Test for the is_normal method
def test_is_normal(zn):
    assert zn.is_normal("H") == True
    

# Test for the order method
def test_order(zn):
    assert zn.order() == 2*n
    
@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 5),
    (3, 5),
    (4, 3)
])
def test_order_element(n, expected):
    assert zn.order_element(n) == expected
    

# Test for the is_abelian method
def test_is_abelian(zn):
    assert zn.is_abelian() == True
    

# Test for the conjugate_class_subgroups method
def test_conjugate_class_subgroups(zn):
    assert  zn.conjugate_class_subgroups() == [(1,2,3),(3,2,4)]

def test_operate(zn):
    assert zn.operate([(1,2,3),(3,2,4)]) == [(1,2,3),(3,2,4)]

def test_cayley_table(zn):
    assert zn.cayley_table() == [(1,2,3)]


# Execute tests with pytest
if __name__ == "__main__":
    pytest.main()


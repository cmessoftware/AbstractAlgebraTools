import pytest
from abstract_math_tools.dihedral_group import dihedral_group


@pytest.fixture
def dg():
    n = 5
    zn =dihedral_group(n)
    return zn
    

def test_is_isomorphic(zn_group):
    assert zn_group.is_isomorphic('H') == True        

# Test for the is_normal method
def test_is_normal(zn_mul_group):
    assert zn_mul_group.is_normal("H") == True
    

# Test for the order method
def test_order(zn_mul_group):
    n = 5
    assert zn_mul_group.order() == 2*n
    

# Test for the order_element method
def test_order_element(zn_mul_group):
    assert zn_mul_group.order_element(1) == 1
    assert zn_mul_group.order_element(2) == 5
    assert zn_mul_group.order_element(3) == 5
    assert zn_mul_group.order_element(4) == 3
    
    

# Test for the is_abelian method
def test_is_abelian(zn_mul_group):
    assert zn_mul_group.is_abelian() == True
    

# Test for the conjugate_class_subgroups method
def test_conjugate_class_subgroups(zn_mul_group):
    assert  zn_mul_group.conjugate_class_subgroups() == [(1,2,3),(3,2,4)]

def test_operate(zn_mul_group):
    assert zn_mul_group.operate([(1,2,3),(3,2,4)]) == [(1,2,3),(3,2,4)]

def test_cayley_graph(zn_mul_group):
    assert zn_mul_group.cayley_graph() == None
    
    
def test_cayley_table(zn_mul_group):
    assert zn_mul_group.cayley_table() == [(1,2,3)]


# Execute tests with pytest
if __name__ == "__main__":
    pytest.main()


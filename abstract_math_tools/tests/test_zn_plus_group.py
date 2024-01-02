import pytest
from abstract_math_tools import zn_plus_group

n = 5

@pytest.fixture
def zn():
    zn_instance = zn_plus_group(n)
    return zn_instance 
    

def test_is_isomorphic(zn_plus_group):
    assert zn_plus_group.is_isomorphic('H') == True        

# Test for the is_normal method
def test_is_normal(zn_plus_group):   
    assert zn_plus_group.is_normal("H") == True
    

# Test for the order method
def test_order(zn_plus_group):
    assert zn_plus_group.order() == 2*n
    

# Test for the order_element method
def test_order_element(zn_plus_group):
    assert zn_plus_group.order_element(1) == 1
    assert zn_plus_group.order_element(2) == 5
    assert zn_plus_group.order_element(3) == 5
    assert zn_plus_group.order_element(4) == 3
    
    

# Test for the is_abelian method
def test_is_abelian(zn_plus_group):
    assert zn_plus_group.is_abelian() == True
    

# Test for the conjugate_class_subgroups method
def test_conjugate_class_subgroups(zn_plus_group):
    assert  zn_plus_group.conjugate_class_subgroups() == [(1,2,3),(3,2,4)]

def test_operate(zn_plus_group):
    assert zn_plus_group.operate([(1,2,3),(3,2,4)]) == [(1,2,3),(3,2,4)]

def test_cayley_graph(zn_plus_group):
    assert zn_plus_group.cayley_graph() == None
    
    
def test_cayley_table(zn_plus_group):
    assert zn_plus_group.cayley_table() == [(1,2,3)]

# Execute tests with pytest
if __name__ == "__main__":
    pytest.main()


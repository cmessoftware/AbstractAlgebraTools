import pytest
from src.group_theory.cyclic_permutation_group import cyclic_permutation_group

@pytest.fixture
def cg():
    n = 5
    zn =cyclic_permutation_group(n)
    return zn
    

def test_is_isomorphic(cg):
    assert cg.is_isomorphic('H') == True        

# Test for the is_normal method
def test_is_normal(cg):
    assert cg.is_normal("H") == True
    

# Test for the order method
def test_order(cg):
    n = 5
    assert cg.order() == 2*n
    

# Test for the order_element method
def test_order_element(cg):
    assert cg.order_element(1) == 1
    assert cg.order_element(2) == 5
    assert cg.order_element(3) == 5
    assert cg.order_element(4) == 3
    
    

# Test for the is_abelian method
def test_is_abelian(cg):
    assert cg.is_abelian() == True
    

# Test for the conjugate_class_subgroups method
def test_conjugate_class_subgroups(cg):
    assert  cg.conjugate_class_subgroups() == [(1,2,3),(3,2,4)]

def test_operate(cg):
    assert cg.operate([(1,2,3),(3,2,4)]) == [(1,2,3),(3,2,4)]

def test_cayley_graph(cg):
    assert cg.cayley_graph() == None
    
    
def test_cayley_table(cg):
    assert cg.cayley_table() == [(1,2,3)]


# Execute tests with pytest
if __name__ == "__main__":
    pytest.main()

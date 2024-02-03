import sys
sys.path.append("../..")
import pytest
from src.group_theory.dihedral_group import dihedral_group


@pytest.fixture
def dg():
    n = 5
    return dihedral_group(n)
    

def test_is_isomorphic(dg):
    assert dg.is_isomorphic('H') == True        

# Test for the is_normal method
def test_is_normal(dg):
    assert dg.is_normal("H") == True
    

# Test for the order method
def test_order(dg):
    n = 5
    assert dg.order() == 2*n
    

@pytest.mark.parametrize("n, expected", [
    (10, 4),
    (15, 8),
    (1, 1),
    (5, 8),
    (11, 98),
])
def test_order_element(dg,n, expected):
    assert dg.order_element(n) == expected
    
    
# Test for the is_abelian method
def test_is_abelian(dg):
    assert dg.is_abelian() == True
    
# Test for the conjugate_class_subgroups method
def test_conjugate_class_subgroups(dg):
    assert  dg.conjugate_class_subgroups() == [(1,2,3),(3,2,4)]

def test_operate(dg):
    assert dg.operate([(1,2,3),(3,2,4)]) == [(1,2,3),(3,2,4)]

def test_cayley_table(dg):
    assert dg.cayley_table() == None
    
    
def test_cayley_table(dg):
    assert dg.cayley_table() == [(1,2,3)]


# Execute tests with pytest
if __name__ == "__main__":
    pytest.main()


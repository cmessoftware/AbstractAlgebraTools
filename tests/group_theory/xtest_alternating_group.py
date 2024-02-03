import sys
sys.path.append("../..")
import pytest
from src.group_theory.alternating_group import alternating_group

n = 5

@pytest.fixture
def ag():
    return alternating_group(n) 


def test_is_isomorphic(ag):
    assert ag.is_isomorphic('H') == True        

# Test for the is_normal method
def test_is_normal(ag):
    assert ag.is_normal("H") == True
    

# Test for the order method
def test_order(ag):
    assert ag.order() == 2*n
    

# Test for the order_element method
def test_order_element(ag):
    assert ag.order_element(1) == 1
    assert ag.order_element(2) == 5
    assert ag.order_element(3) == 5
    assert ag.order_element(4) == 3
    
    

# Test for the is_abelian method
def test_is_abelian(ag):
    assert ag.is_abelian() == True
    

# Test for the conjugate_class_subgroups method
def test_conjugate_class_subgroups(ag):
    assert  ag.conjugate_class_subgroups() == [(1,2,3),(3,2,4)]

def test_operate(ag):
    assert ag.operate([(1,2,3),(3,2,4)]) == [(1,2,3),(3,2,4)]

def test_cayley_graph(ag):
    assert ag.cayley_graph() == None
    
    
def test_cayley_table(ag):
    assert ag.cayley_table() == [(1,2,3)]


# Execute tests with pytest
if __name__ == "__main__":
    pytest.main()


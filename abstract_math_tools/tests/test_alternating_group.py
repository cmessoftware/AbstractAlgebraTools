import pytest
from abstract_math_tools import alternating_group

n = 5

@pytest.fixture
def ag():
    return alternating_group(n) 


def test_is_isomorphic(alternating_group):
    assert alternating_group.is_isomorphic('H') == True        

# Test for the is_normal method
def test_is_normal(alternating_group):
    assert alternating_group.is_normal("H") == True
    

# Test for the order method
def test_order(alternating_group):
    assert alternating_group.order() == 2*n
    

# Test for the order_element method
def test_order_element(alternating_group):
    assert alternating_group.order_element(1) == 1
    assert alternating_group.order_element(2) == 5
    assert alternating_group.order_element(3) == 5
    assert alternating_group.order_element(4) == 3
    
    

# Test for the is_abelian method
def test_is_abelian(alternating_group):
    assert alternating_group.is_abelian() == True
    

# Test for the conjugate_class_subgroups method
def test_conjugate_class_subgroups(alternating_group):
    assert  alternating_group.conjugate_class_subgroups() == [(1,2,3),(3,2,4)]

def test_operate(alternating_group):
    assert alternating_group.operate([(1,2,3),(3,2,4)]) == [(1,2,3),(3,2,4)]

def test_cayley_graph(alternating_group):
    assert alternating_group.cayley_graph() == None
    
    
def test_cayley_table(alternating_group):
    assert alternating_group.cayley_table() == [(1,2,3)]


# Execute tests with pytest
if __name__ == "__main__":
    pytest.main()


import pytest
from src.group_theory.gl_group import gl_group

@pytest.fixture
def gl():
    n = 5
    return gl_group(n)
    

def test_is_isomorphic(gl):
    assert gl.is_isomorphic('H') == True        

# Test for the is_normal method
def test_is_normal(gl):
    assert gl.is_normal("H") == True
    

# Test for the order method
def test_order(gl):
    n = 5
    assert gl.order() == 2*n
    

# Test for the order_element method
def test_order_element(gl):
    assert gl.order_element(1) == 1
    assert gl.order_element(2) == 5
    assert gl.order_element(3) == 5
    assert gl.order_element(4) == 3
    
    

# Test for the is_abelian method
def test_is_abelian(gl):
    assert gl.is_abelian() == True
    

# Test for the conjugate_class_subgroups method
def test_conjugate_class_subgroups(gl):
    assert  gl.conjugate_class_subgroups() == [(1,2,3),(3,2,4)]

def test_operate(gl):
    assert gl.operate([(1,2,3),(3,2,4)]) == [(1,2,3),(3,2,4)]

def test_cayley_graph(gl):
    assert gl.cayley_graph() == None
    
    
def test_cayley_table(gl):
    assert gl.cayley_table() == [(1,2,3)]


# Execute tests with pytest
if __name__ == "__main__":
    pytest.main()


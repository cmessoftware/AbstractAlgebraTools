import pytest
from src.group_theory.klein_group import klein_group

@pytest.fixture
def kg():
    n = 5
    return klein_group(n)
  
def test_is_isomorphic(kg):
    assert kg.is_isomorphic('H') == True        

# Test for the is_normal method
def test_is_normal(kg):
    assert kg.is_normal("H") == True
    

# Test for the order method
def test_order(kg):
    n = 5
    assert kg.order() == 2*n
    

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 5),
    (3, 5),
    (4, 3)
])
def test_order_element(kg,n, expected):
    assert kg.order_element(n) == expected
    

# Test for the is_abelian method
def test_is_abelian(kg):
    assert kg.is_abelian() == True
    

# Test for the conjugate_class_subgroups method
def test_conjugate_class_subgroups(kg):
    assert  kg.conjugate_class_subgroups() == [(1,2,3),(3,2,4)]

def test_operate(kg):
    assert kg.operate([(1,2,3),(3,2,4)]) == [(1,2,3),(3,2,4)]

    
def test_cayley_table(kg):
    assert kg.cayley_table() == [(1,2,3)]


# Execute tests with pytest
if __name__ == "__main__":
    pytest.main()


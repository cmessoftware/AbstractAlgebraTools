import sys
sys.path.append("../..")
import pytest
from  src.group_theory.zn_group import zn_group

n = 4

@pytest.fixture 
def zn():
    return zn_group(n)
 
@pytest.mark.parametrize("H, expected", [
    ([10,100,1000,10000], True),
    ([1,2,3,4], True)
])   
def test_is_isomorphic(zn,H,expected):  
    assert zn.is_isomorphic(H) == expected

@pytest.mark.parametrize("a, expected", [
    ([2*i for i in range(1,n+1)], True),
    ([5*i for i in range(1,n+1)], True),
    ([10*i for i in range(1,n+1)], True),
    ([11*i for i in range(1,n+1)], True), 
    ([21*i for i in range(1,n+1)], True), 
])
def test_is_normal(zn: zn_group,a,expected):   
    assert zn.is_normal(a) == expected
  
     
@pytest.mark.parametrize("a, expected", [
    (10, 2),
    (17, 4),
    (34,2),
    (33, 4), 
    (269, 4), 
    (52, 2), 
    (639, 4), 
    (0, 1),
])
# Test for the order method
def test_order_element(zn,a,expected):
    assert zn.order_element(a) == expected

@pytest.mark.parametrize("G, expected", [
    ([2*i for i in range(1,n+1)], n),
    ([5*i for i in range(1,n+1)], n),
    ([10*i for i in range(1,n+1)], n),
    ([11*i for i in range(1,n+1)], n), 
    ([21*i for i in range(1,n+1)], n), 
])
def test_order(zn,G,expected):
    assert zn.order(G) == expected

@pytest.mark.parametrize("a, expected", [
([1],[1]),
([i for i in range(11)], [2,3,4,5,6,7,8,9,10]),
([i for i in range(21)], [8, 13, 20]),
([i for i in range(15)], [4, 11, 14]),
([i for i in range(33)], [10, 23, 32]), 
])    
def test_gens(zn: zn_group,a, expected):
    assert zn.gens(a) == expected
    
 
# Test for the is_abelian method
def test_is_abelian(zn: zn_group):
    assert zn.is_abelian() == True
    
@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3,3),
])
def test_cardinality(zn,n,expected):
    assert zn.cardinality(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3,3),
])
def test_conjugate_class_subgroups(zn,n,expected):
    assert  zn.conjugate_class_subgroups(n) == expected


@pytest.mark.parametrize("a,b, expected", [
    (1,2,3%n),
    (2,-2,0),
    (3,6,9%n),
    (5, 120, 125%n), 
    (269, 246, 515%n),
    (52, 80, 132%n), 
    (63, 38, 101%n), 
])
def test_binary_operation(zn,a,b,expected):
    assert zn.binary_operation(a,b) == expected

    
def test_cayley_table(zn: zn_group):
    assert zn.cayley_table() == [(1,2,3)]

# Execute tests with pytest
if __name__ == "__main__":
    pytest.main()


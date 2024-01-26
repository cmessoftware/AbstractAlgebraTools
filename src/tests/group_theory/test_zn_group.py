import pytest
from  src.group_theory.zn_group import zn_group

n = 4

@pytest.fixture
def zn():
    return zn_group(n)
 
@pytest.mark.parametrize("a, expected", [
    # (('a','b','c','d'), True),
    # (('a','b','c'), False),
    ([10,100,1000,10000], True),
    ([1,2,3,4], True),
])   
def test_is_isomorphic(zn,a,expected):
    assert zn.is_isomorphic(a) == expected


def test_is_normal(zn: zn_group,a,expected):   
    assert zn.is_normal(a) == expected
    
@pytest.mark.parametrize("a, expected", [
    (10, 2),
    (17, 4),
    (34,2),
    (33, 4), 
    (269, 4), 
    (52, 1), 
    (636, 1), 
])
# Test for the order method
def test_order(zn,a,expected):
    assert zn.order(a) == expected

@pytest.mark.parametrize("a, expected", [
(1,[1]),
(45,[1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44]),
(100,[1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39, 41, 43, 47, 49, 51, 53, 57, 59, 61, 63, 67, 69, 71, 73, 77, 79, 81, 83, 87, 89, 91, 93, 97, 99]),
(27,[1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26]),
(190,[1, 3, 7, 9, 11, 13, 17, 21, 23, 27, 29, 31, 33, 37, 39, 41, 43, 47, 49, 51, 53, 59, 61, 63, 67, 69, 71, 73, 77, 79, 81, 83, 87, 89, 91, 93, 97, 99, 101, 103, 107, 109, 111, 113, 117, 119, 121, 123, 127, 129, 131, 137, 139, 141, 143, 147, 149, 151, 153, 157, 159, 161, 163, 167, 169, 173, 177, 179, 181, 183, 187,189])
])    
def test_gens(zn: zn_group):
    assert zn.gens() == [1]
    
 
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

def test_conjugate_class_subgroups(zn,expected):
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


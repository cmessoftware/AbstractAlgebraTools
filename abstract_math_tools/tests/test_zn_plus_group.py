import pytest
from abstract_math_tools.zn_plus_group import zn_plus_group

n = 4

@pytest.fixture
def zn():
    return zn_plus_group(n)
    
def test_is_isomorphic(zn: zn_plus_group):
    assert zn.is_isomorphic('H') == True        

# Test for the is_normal method
def test_is_normal(zn: zn_plus_group):   
    assert zn.is_normal("H") == True
    
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
    
def test_gens(zn: zn_plus_group):
    assert zn.gens() == [1]
    
 
# Test for the is_abelian method
def test_is_abelian(zn: zn_plus_group):
    assert zn.is_abelian() == True
    
@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3,6),
    (5, 120), 
    (269, 24674496683959639479411192502726424547294255297332825680197106039081288901892917898390428994254364001014736124508189279001775937834782944634392375598803528916550589946813690011829690208985566315900911455090647265355232802576460150612022157794389597509558870312080150047612904606819941984627269241198574206484947062512313239769846257455041082292703331013802572428307093284564192341826933936748033736435797155358322718943252370260495773262171506529862911305849523210563459481600000000000000000000000000000000000000000000000000000000000000000), 
    (52, 80658175170943878571660636856403766975289505440883277824000000000000), 
    (636, 387534577628655132694434773461951082204814793624420670405249410404201382876183727490054086231157061227691150689093715105130135270490296531189481626514539505733785929078005418680147065019716829520679626206682184211795813772044457949286946852315306397318351478979795689846373993658547069445004648482343096264976899782489435554846804278385360400736003865672773646241140001246766942160837249546667269688112300361875666385593198834700761001692969512751710420928847027955376107561220384545801910259638041404481985162240050551693878604173364000119093828211299266730646751880319539811478100402574919412433675574405214690790376807696449433240054512849097703456244411021513102854687526659496161568786920416922397491360740648183844292001640987762176829001729604830729467533853694852516948962486188434628870020827397653255017733470053706407497461362283641565889254886930591671428181046199403623261342190026142011302675714007664449957200524401554548005885411621336302822350320482907953309256601311283039981130437269805154399282776309469329921649748329083200743051770207134932530130365681934010229836030115023229457645816321833421835463129182070896865141105113070928827165037654883989027738546844873096979428069084640501183947110222653027904899053139005794493777203278358853417434078673068118408140538771763512476601712356272736766713665551105282377673145957797068800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000), 
])
def test_cardinality(zn,n, expected):
    assert zn.cardinality(n) == expected

@pytest.mark.parametrize("expected", [
        ([[(4, 3, 2, 1), (1, 2, 4, 3)], [(4, 2, 3, 1), (1, 2, 4, 3)], [(4, 1, 3, 2), (1, 2, 4, 3)], [(3, 4, 2, 1), (1, 2, 4, 3)], [(3, 2, 4, 1), (1, 2, 4, 3)], [(3, 1, 4, 2), (1, 2, 4, 3)], [(2, 4, 3, 1), (1, 2, 4, 3)], [(2, 3, 4, 1), (1, 2, 4, 3)], [(2, 1, 4, 3), (1, 2, 4, 3)], [(1, 4, 3, 2), (1, 2, 4, 3)], [(1, 3, 4, 2), (1, 2, 4, 3)], [(1, 2, 4, 3)], [(1, 2, 3, 4)]]),
    ])
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

    
def test_cayley_table(zn: zn_plus_group):
    assert zn.cayley_table() == [(1,2,3)]

# Execute tests with pytest
if __name__ == "__main__":
    pytest.main()


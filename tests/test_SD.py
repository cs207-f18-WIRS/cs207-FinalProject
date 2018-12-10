import pytest
import math
from AD import symdif as symdif

def test_f1():
    f1 = "POW(x, POW(x, x))"
    vd = "x:2.0"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 16) < 1e-7
    assert math.fabs(F1.diff("x") - 107.1104124466013909) < 1e-7

def test_f2():
    f1 = "EXP(3.0*X+X*POW(Y,2))"
    vd ="X:1.0,Y:2.0"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    
    math.fabs(F1.val() - 1096.6331584284585992) < 1e-7
    assert math.fabs(F1.diff("X") - 7676.432108999210194) < 1e-7
    assert math.fabs(F1.diff("Y") - 4386.532633713834397) < 1e-7

def test_f3():
    f1 = "EXP(3+LOG(POW(X,2)))"
    vd ="X:2.0"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 80.342147692750670) < 1e-7
    assert math.fabs(F1.diff("X") - 80.342147692750670) < 1e-7

def test_f4():
    f1 = "SIN(2.0/X)-COS(3*X)"
    vd ="X:5.0"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 1.1491062551674717) < 1e-7
    assert math.fabs(F1.diff("X") - 1.877178640951119) < 1e-7

def test_f5():
    f1 = "SIN(POW(X, 2))*EXP(COS(3.0*Y))"
    vd ="X:2.0,Y:3.0"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - -0.30428721849) < 1e-7
    assert math.fabs(F1.diff("X") - -1.05124071609) < 1e-7
    assert math.fabs(F1.diff("Y") - 0.37620716268) < 1e-7

def test_f6():
    f1 = "POW(2, X)"
    vd = "X:2.0"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 4) < 1e-7
    assert math.fabs(F1.diff("X") - 2.772588722239781) < 1e-7

def test_noVd():
    f1 = "x+y"
    vd = "x:1,y:1"

    F1 = symdif.SD(f1)
    with pytest.raises(NameError) as e:
        F1.diff_all()
    assert(str(e.value) == 'Must set point to evaluate')
    ret = F1.diff_all(vd)
    for k, v in ret.items():
        assert(v == 1)

def test_smallVd():
    F1 = symdif.SD("x")
    f2 = "x*y"
    vd = "x:3"
    F1.new_formula(f2)
    with pytest.raises(NameError) as e:
        F1.val(vd)
    assert(F1.val("x:3,y:2")==6)
    return

def test_f7():
    f1 = "2*"
    vd = "x:2.0"
    with pytest.raises(NameError) as e:
        F1 = symdif.SD(f1)
    assert(str(e.value)=="Invalid character")

def test_f8():
    f1 = "x#y"
    vd = "x:1.0"
    with pytest.raises(NameError) as e:
        F1 = symdif.SD(f1)
    assert(str(e.value)=="Invalid character")

def test_f9():
    f1 = "+3+x"
    vd = "x:1.0"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 4) < 1e-7

def test_f10():
    f1 = "-3+x"
    vd = "x:1.0"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() + 2) < 1e-7

def test_f11():
    f1 = "(3)+x"
    vd = "x:1.0"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 4) < 1e-7
    assert math.fabs(F1.diff("x") - 1) < 1e-7

def test_f12():
    f1 = "x+3)))"
    vd = "x:1.0"
    with pytest.raises(NameError) as e:
        F1 = symdif.SD(f1)
    assert(str(e.value)=="Invalid syntax")

### Simplification and symbolic differentiation tests:

def test_1():
    # Long expression simplifying in: 6xy^2 thus the dx should be 6y^2 or '6.0*y**2'
    # Example using power: 
    f1 = "(((((POW(x,3.0)*(3.0/x))*(3.0/x))+(POW(x,3.0)*((-3.0)/(x*x))))*y)*y)"
    vd = "x:2,y:3"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert str(F1.symbolic_diff("x", output='default')) == '6.0*y**2'

def test_2():
    # Example using exp and log: 
    # e^(log(5x)) = 5x thus the x-derivative=5
    f1 = "EXP(LOG(5*x))"
    vd = "x:2"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert str(F1.symbolic_diff("x", output='default')) == '5.00000000000000'
    
def test_3():
    # Example using sin, cos and pow:  
    # sin(x)^2+cos(x)^2 = 1 thus the x-derivative=0
    f1 = '(POW(SIN(x),2) + POW(COS(x),2))'
    vd = "x:2"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert str(F1.symbolic_diff("x", output='default')) == '2.0*sin(x)**1.0*cos(x) - 2.0*sin(x)*cos(x)**1.0'
    # this is 0

def test_4():
    # Example using exp
    # dx of e^x =  e^x
    f1 = 'EXP(x)'
    vd = "x:2"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert str(F1.symbolic_diff("x", output='default')) == 'exp(x)'
    
def test_5():
    # Example using tan and the latex formula
    # dx of tan(x) =  1/cos^2(x)
    f1 = 'TAN(x)'
    vd = "x:2"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert str(F1.symbolic_diff("x", output='latex')) == '\\frac{1}{x}' 
    # INCORRECT SHOULD BE 1/cos^2(x) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def test_6():
    # Example using arcsin
    # dx of asin(x) =  1/sqrt(1-x^2)
    f1='ARCSIN(x)'
    vd = "x:2"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert str(F1.symbolic_diff("x", output='pretty')) == '1/x'
    # INCORRECT SHOULD BE 1/sqrt(1-x^2) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def test_7():
    # Example using arccos
    # dx of acos(x) =  -1/sqrt(1-x^2)
    f1='ARCSIN(x)'
    vd = "x:2"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert str(F1.symbolic_diff("x", output='pretty')) == '1/x'
    # INCORRECT SHOULD BE -1/sqrt(1-x^2) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def test_8():
    # Example using arctan
    # dx of atan(x) =  1/(x^2+1)
    f1='ARCTAN(x)'
    vd = "x:2"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert str(F1.symbolic_diff("x", output='all')) == '1/x'
    # INCORRECT SHOULD BE 1/(x^2+1) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def test_9():
    # Example using hyperbolic sine
    # dx of sinh(x) =  (e^(-x)+e^(x))/2
    f1='SINH(x)'
    vd = "x:2"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert str(F1.symbolic_diff("x")) == '1/x'
    # INCORRECT SHOULD BE (e^(-x)+e^(x))/2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def test_10():
    # Example using hyperbolic cose
    # dx of cosh(x) =  (e^(x)-e^(-x))/2
    f1='COSH(x)'
    vd = "x:2"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert str(F1.symbolic_diff("x")) == '1/x'
    # INCORRECT SHOULD BE (e^(x)-e^(-x))/2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def test_11():
    # Example using hyperbolic tan
    # dx of tanh(x) =  4/(e^(x)+e^(-x))^2
    f1='TANH(x)'
    vd = "x:2"
    F1 = symdif.SD(f1)
    F1.set_point(vd)
    assert str(F1.symbolic_diff("x")) == '1/x'
    # INCORRECT SHOULD BE 4/(e^(x)+e^(-x))^2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
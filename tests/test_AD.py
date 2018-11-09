import pytest
import math
from AD import autodif as autodif

def test_f1():
    f1 = "POW(x, POW(x, x))"
    vd = "x:2.0"
    F1 = autodif.AD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 16) < 1e-7
    assert math.fabs(F1.diff("x") - 107.1104124466013909) < 1e-7

def test_f2():
    f1 = "EXP(3.0*X+X*POW(Y,2))"
    vd ="X:1.0,Y:2.0"
    F1 = autodif.AD(f1)
    F1.set_point(vd)
    
    math.fabs(F1.val() - 1096.6331584284585992) < 1e-7
    assert math.fabs(F1.diff("X") - 7676.432108999210194) < 1e-7
    assert math.fabs(F1.diff("Y") - 4386.532633713834397) < 1e-7

def test_f3():
    f1 = "EXP(3+LOG(POW(X,2)))"
    vd ="X:2.0"
    F1 = autodif.AD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 80.342147692750670) < 1e-7
    assert math.fabs(F1.diff("X") - 80.342147692750670) < 1e-7

def test_f4():
    f1 = "SIN(2.0/X)-COS(3*X)"
    vd ="X:5.0"
    F1 = autodif.AD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 1.1491062551674717) < 1e-7
    assert math.fabs(F1.diff("X") - 1.877178640951119) < 1e-7

def test_f5():
    f1 = "SIN(POW(X, 2))*EXP(COS(3.0*Y))"
    vd ="X:2.0,Y:3.0"
    F1 = autodif.AD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - -0.30428721849) < 1e-7
    assert math.fabs(F1.diff("X") - -1.05124071609) < 1e-7
    assert math.fabs(F1.diff("Y") - 0.37620716268) < 1e-7

def test_f6():
    f1 = "POW(2, X)"
    vd = "X:2.0"
    F1 = autodif.AD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 4) < 1e-7
    assert math.fabs(F1.diff("X") - 2.772588722239781) < 1e-7

def test_noVd():
    f1 = "x+y"
    vd = "x:1,y:1"

    F1 = autodif.AD(f1)
    with pytest.raises(NameError) as e:
        F1.diff_all()
    assert(str(e.value) == 'Must set point to evaluate')
    ret = F1.diff_all(vd)
    for k, v in ret.items():
        assert(v == 1)

def test_smallVd():
    F1 = autodif.AD("x")
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
        F1 = autodif.AD(f1)
    assert(str(e.value)=="Invalid character")

def test_f8():
    f1 = "x#y"
    vd = "x:1.0"
    with pytest.raises(NameError) as e:
        F1 = autodif.AD(f1)
    assert(str(e.value)=="Invalid character")

def test_f9():
    f1 = "+3+x"
    vd = "x:1.0"
    F1 = autodif.AD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 4) < 1e-7
    assert math.fabs(F1.diff("x") - 1) < 1e-7

def test_f10():
    f1 = "-3+x"
    vd = "x:1.0"
    F1 = autodif.AD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() + 2) < 1e-7
    assert math.fabs(F1.diff("x") - 1) < 1e-7

def test_f11():
    f1 = "(3)+x"
    vd = "x:1.0"
    F1 = autodif.AD(f1)
    F1.set_point(vd)
    assert math.fabs(F1.val() - 4) < 1e-7
    assert math.fabs(F1.diff("x") - 1) < 1e-7

def test_f12():
    f1 = "x+3)))"
    vd = "x:1.0"
    with pytest.raises(NameError) as e:
        F1 = autodif.AD(f1)
    assert(str(e.value)=="Invalid character")

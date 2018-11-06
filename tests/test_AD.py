import pytest
from interpreter import Lexer, Parser, Interpreter

def test_f1():
    f1 = "POW(x, POW(x, x))";
    vd = "x:2";
    lexer = Lexer(f1);
    parser = Parser(lexer);
    interpreter = Interpreter(parser);
    dx=interpreter.differentiate(vd, dv='x');
    assert dx==107.1104124466013909813974174582298585475873975011072538

def test_f2():
    f1 = "EXP(3*X+X*POW(Y,2))";
    vd ="X:1,Y:2";
    lexer = Lexer(f1);
    parser = Parser(lexer);
    interpreter = Interpreter(parser);
    dx=interpreter.differentiate(vd, dv='X');
    dy=interpreter.differentiate(vd, dv='Y');
    assert dx==7676.432108999210194846041668016850027095533943835292006
    assert dy==4386.532633713834397054880953152485729768876539334452575

def test_f3():
    f1 = "EXP(3+LOG(POW(X,2)))";
    vd ="X:2";
    lexer = Lexer(f1);
    parser = Parser(lexer);
    interpreter = Interpreter(parser);
    dx=interpreter.differentiate(vd, dv='X');
    assert dx==80.342147692750670963714118618326871587951631354216600577

def test_f4():
    f1 = "SIN(2/X)-COS(3*X)";
    vd ="X:5";
    lexer = Lexer(f1);
    parser = Parser(lexer);
    interpreter = Interpreter(parser);
    dx=interpreter.differentiate(vd, dv='X');
    assert dx==1.877178640951119790865338674402466846521587000496647133

def test_f5():
    f1 = "SIN(POW(X, 2))*EXP(COS(3*Y))";
    vd ="X:2,Y:3";
    lexer = Lexer(f1);
    parser = Parser(lexer);
    interpreter = Interpreter(parser);
    dx=interpreter.differentiate(vd, dv='X');
    dy=interpreter.differentiate(vd, dv='Y');
    assert dx==10.71391946063094313319444375622570288650375264167699750
    assert dy==-0.08789937978525762958460081495689783503136765274262355

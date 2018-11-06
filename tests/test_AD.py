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
    
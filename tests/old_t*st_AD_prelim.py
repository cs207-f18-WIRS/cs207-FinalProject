import sys
sys.path.append('../AD')

from interpreter import Lexer, Parser, Interpreter

f1 = "POW(x, POW(x, x))";
vd = "x:2";
lexer = Lexer(f1);
parser = Parser(lexer);
interpreter = Interpreter(parser);
print('\nCalculating dif of {}, at {}'.format(f1, vd))
interpreter.diff_all(vd);
print('According to Wolfram Alpha this should give:\n32 (1 + 2 log^2(2) + log(4))=107.1104124466013909813974174582298585475873975011072538')

f1 = "EXP(3*X+X*POW(Y,2))";
vd ="X:1,Y:2";
lexer = Lexer(f1);
parser = Parser(lexer);
interpreter = Interpreter(parser);
print('\nCalculating dif of {}, at {}'.format(f1, vd))
interpreter.diff_all(vd);

print('According to Wolfram Alpha this should give:\n7*e^7=7676.432108999210194846041668016850027095533943835292006\n4*e^7=4386.532633713834397054880953152485729768876539334452575')

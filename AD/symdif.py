import AD.interpreter as ast
import sympy

class SD():
    """
    User friendly interface for the AST interpreter.
    Usage
    =============
    import symdif
    def main():
        f1 = "x*y*z"
        vd = "x:2,y:3,z:4"
        F1 = symdif.SD(f1)
        print(F1.diff_all(vd))
        print(F1.diff("x"))
        F1.new_formula("a+b")
        vd = "a:10, b : 1"
        F1.set_point(vd)
        print(F1.val())
        print(F1.diff_all())

        // higher order derivative
        f1 = "x*x*x*y*y"
        vd = "x:2,y:3"
        F1 = autodif.AD(f1)
        F1.set_point(vd)
        ret = F1.diff("x", order=3)
        print(ret)
        ret = F1.diff("y", order=2)
        print(ret)
    
        // symbolic differentiation
        f1 = "POW(x,3.0)*3.0/x*3.0/x+POW(x,3.0)*(3.0)/x/x/y/y"
        vd = "x:2,y:3"
        F1 = symdif.SD(f1)
        F1.set_point(vd)
        F1.symbolic_diff("x", output='default')
           output: '9.0 + 3.0/y**2'
        F1.symbolic_diff("x", output='latex')
           output: '9.0 + \\frac{3.0}{y^{2}}'
        F1.symbolic_diff("x", output='pretty')
                         3.0
           output: 9.0 + ---
                           2
                         y
        F1.symbolic_diff("x", output='all') # to print all the results
    """

    def __init__(self, frmla):
        self.formula = frmla
        self.lexer = ast.Lexer(frmla)
        self.parser = ast.Parser(self.lexer)
        self.interpreter = ast.Interpreter(self.parser)
        self.vd = None

    def set_point(self, vd):
        if vd is not None:
            self.vd = vd
        if self.vd is None:
            raise NameError("Must set point to evaluate")
    
    def diff(self, dv, vd=None, order=1):
        self.set_point(vd)
        new_interpreter = self.interpreter
        for i in range(order-1):
            new_frmla = new_interpreter.symbolic_diff(self.vd, dv)
            new_lexer = ast.Lexer(new_frmla)
            new_parser = ast.Parser(new_lexer)
            new_interpreter = ast.Interpreter(new_parser)
        return new_interpreter.differentiate(self.vd, dv)
    
    def symbolic_diff(self, dv, vd=None, order=1, output='default'):
        self.set_point(vd)
        new_interpreter = self.interpreter
        for i in range(order-1):
            new_frmla = new_interpreter.symbolic_diff(self.vd, dv)
            new_lexer = ast.Lexer(new_frmla)
            new_parser = ast.Parser(new_lexer)
            new_interpreter = ast.Interpreter(new_parser)
        formul = new_interpreter.symbolic_diff(self.vd, dv)
        simplified = self.symplify(formul, output)
        return simplified
    
    def diff_all(self, vd=None):
        self.set_point(vd)
        return self.interpreter.diff_all(self.vd)
    
    def val(self, vd=None):
        self.set_point(vd)
        return self.interpreter.interpret(self.vd)
    
    def new_formula(self, frmla):
        self.formula = frmla
        self.lexer = ast.Lexer(frmla)
        self.parser = ast.Parser(self.lexer)
        self.interpreter = ast.Interpreter(self.parser)
        self.vd = None

    def symplify(self, formul, output):
        def POW(a, b):
            return a ** b
            
        def EXP(a):
            return sympy.exp(a)
            
        def LOG(a):
            return sympy.log(a)
            
        def COS(a):
            return sympy.cos(a)
            
        def SIN(a):
            return sympy.sin(a)
            
        def TAN(a): # Tangent Function
            return sympy.tan(a)
            
        def ARCSIN(a): # Inverse trigonometric functions: inverse sine or arcsine    
            return sympy.asin(a)
            
        def ARCCOS(a): # Inverse trigonometric functions: inverse cosine or arccosine    
            return sympy.acos(a)
            
        def ARCTAN(a): # Inverse trigonometric functions: inverse tangent or arctangent    
            return sympy.atan(a)

        def SINH(a): # Inverse trigonometric functions: inverse sine or arcsine
            return sympy.sinh(a)
            
        def COSH(a): # Inverse trigonometric functions: inverse cosine or arccosine    
            return sympy.cosh(a)
            
        def TANH(a): # Inverse trigonometric functions: inverse tangent or arctangent    
            return sympy.tanh(a)
               
        string_for_sympy=""
        string_for_sympy2=""
        split_variables=self.vd.split(",")
        
        for var in split_variables:
            l=var.split(":")
            string_for_sympy=string_for_sympy+l[0]+" "	
            string_for_sympy2=string_for_sympy2+l[0]+", "
            
        exec(string_for_sympy2[:-2] + "= sympy.symbols('" + string_for_sympy+ "')")
            
        if output == 'default':
            return sympy.simplify(eval(formul))
            
        if output == 'latex':
            return sympy.latex(sympy.simplify(eval(formul)))
            
        if output == 'pretty':
            sympy.pprint(sympy.simplify(eval(formul)))
            return sympy.simplify(eval(formul))
            
        if output == 'all':
            print('\nSymbolic differentiation result:')
            print(formul)
            print('\nSimplified Pretty Print:\n') ; sympy.pprint(sympy.simplify(eval(formul)))
            print('\nSimplified Latex code:')
            print(sympy.latex(sympy.simplify(eval(formul))))
            print('\nSimplified Default:')
            print(sympy.simplify(eval(formul)),'\n')
            return sympy.simplify(eval(formul))
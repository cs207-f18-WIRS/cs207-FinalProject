""" SPI - Simple Pascal Interpreter """
import copy

###############################################################################
#                                                                             #
#  LEXER                                                                      #
#                                                                             #
###############################################################################

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF, VAR = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF', 'VAR'
)


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def word(self):
        """Return a multichar integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isalpha():
            result += self.current_char
            self.advance()
        return  result

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            
            if self.current_char.isalpha():
                return Token(VAR, self.word())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            self.error()

        return Token(EOF, None)


###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################

class AST(object):
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Var(AST):
    def __init__(self, token):
        self.token = token
        self.name = token.value

class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : (PLUS | MINUS) factor | INTEGER | VAR | LPAREN expr RPAREN"""
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == MINUS:
            self.eat(MINUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == VAR:
            self.eat(VAR)
            return Var(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        """
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN
        """
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self):
        node = self.expr()
        if self.current_token.type != EOF:
            self.error()
        return node

    def dfactor(self):
        """factor : (PLUS | MINUS) factor | INTEGER | VAR | LPAREN expr RPAREN"""
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            node = UnaryOp(token, self.dfactor())
            return node, node
        elif token.type == MINUS:
            self.eat(MINUS)
            node = UnaryOp(token, self.dfactor())
            return node, node
        elif token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token), Num(Token(INTEGER, 0))
        elif token.type == VAR:
            self.eat(VAR)
            return Var(token), Var(Token(VAR, "d_" + token.value))
        elif token.type == LPAREN:
            self.eat(LPAREN)
            cur = copy.deepcopy(self)
            node = self.expr()
            dnode = cur.dexpr()
            self.eat(RPAREN)
            return node, dnode  

    def dterm(self):
        """term : factor ((MUL | DIV) factor)*"""
        node, dnode = self.dfactor()
        print(node.token)
        print(dnode.token)

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)
            
            rnode, rdnode = self.dfactor()
            print(rnode, rdnode)
            lowdhi = BinOp(left=dnode, op=Token(MUL,'*'), right=rnode)
            hidlow = BinOp(left=node, op=Token(MUL,'*'), right=rdnode)
            if token.type == MUL:
                # chain rule
                dnode = BinOp(left=lowdhi, op=Token(PLUS,'+'), right=hidlow)
                node = BinOp(left=node, op=Token(MUL,'*'), right=rnode)
            else:
                # quotient rule
                topnode = BinOp(left=lowdhi, op=Token(MINUS, '-'), right=hidlow)
                botnode = BinOp(left=rnode, op=Token(MUL,'*'), right=rnode)
                dnode = BinOp(left=topnode, op=Token(DIV,'/'), right=botnode)
                node = BinOp(left=node, op=Token(DIV,'/'), right=rnode)
        return dnode

    def dexpr(self):
        """
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN
        """
        dnode = self.dterm()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            dnode = BinOp(left=dnode, op=token, right=self.dterm())
        print(dnode)
        return dnode

    
    def dparse(self):
        node = self.dexpr()
        if self.current_token.type != EOF:
            self.error()
        return node

###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################

class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def visit_Var(self, node):
        if self.vardict is None:
            raise NameError("no var dict passed in")
        if node.name not in self.vardict:
            raise NameError("var {} not in var dict".format(node.name))
        return self.vardict[node.name]

    def visit_UnaryOp(self, node):
        op = node.op.type
        if op == PLUS:
            return +self.visit(node.expr)
        elif op == MINUS:
            return -self.visit(node.expr)

    def interpret(self):
        self.get_vardict()
        tree = self.parser.parse()
        if tree is None:
            return ''
        return self.visit(tree)
    
    def differentiate(self):
        self.get_vardict()
        self.get_diffvar()
        tree = self.parser.dparse()
        if tree is None:
            return ''
        return self.visit(tree)

    def get_vardict(self):
        """ expects vardict to be formatted as x:10, y:20, z:3 """
        vdict = {}
        text = input('vardict> ')
        if not text:
            self.vardict = None
            return
        text = text.replace(" ", "")
        for var in text.split(','):
            vals = var.split(':')
            vdict[str(vals[0])] = int(vals[1])
        self.vardict = vdict
        return
    
    def get_diffvar(self):
        text = input('d_var> ')
        text = text.replace(" ", "")
        if text not in self.vardict.keys():
            raise NameError("d_var not in vardict")
        for v in list(self.vardict.keys()):
            self.vardict["d_"+v]=0
        self.vardict["d_"+text]=1
        return
        


def main():
    while True:
        try:
            try:
                text = raw_input('spi> ')
            except NameError:  # Python3
                text = input('spi> ')
        except EOFError:
            break
        if not text:
            continue

        vardict = {"x":10}
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.differentiate()
        print(result)

if __name__ == '__main__':
    main()
    
'''
Based off of the open source tutorial: Let's Build a Simple Interpreter
https://github.com/rspivak/lsbasi/tree/master/part8/python
'''

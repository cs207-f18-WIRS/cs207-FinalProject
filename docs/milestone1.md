## Milestone1 Document
You must clearly outline your software design for the project.  Here are some possible sections to
include in your document along with some prompts that you may want to address.

### Introduction
Describe problem the software solves and why it's important to solve that problem
 - TODO

### Background
Describe (briefly) the mathematical background and concepts as you see fit.  You **do not** need to
give a treatise on automatic differentation or dual numbers.  Just give the essential ideas (e.g.
the chain rule, the graph structure of calculations, elementary functions, etc).
 - TODO
 
### How to Use AD
How do you envision that a user will interact with your package?  What should they import?  How can
they instantiate AD objects?

The user should type the following commands in the python:
```python
>>> import AD as grad         # Import module
>>> f='e^(x^2)+y'             # Create a function
>>> varlist=[x,y]             # Define list of variables in f
>>> AD_obj=grad(f,varlist)    # Instatiate AD object ( if grad(f,varlist) can't parse f as a valid function raise exception)
>>> AD_obj([1.0,2])           # Calculate the automatic differentation at x=1.0 and y=2.0 (only if len(list)=len(varlist))
```

**Note: This section should be a mix of pseudo code and text.  It should not include any actual
operations yet.**

### Software Organization
Discuss how you plan on organizing your software package.
* Directory Structure:
home_directory
  - AD 
    - AST_builder/parser
    - Differentiator
    - Interface
  - Tests
    - AST_builder/parser test
    - Differentiator test
    - Interface test
  - Documention
  - Examples
  
* What modules do you plan on including?  What is their basic functionality?
  - We will use and expand a parser from "https://ruslanspivak.com/lsbasi-part7/". Currently, this parser only handles parsing and evaluating basic arithmetic operations with numbers. We will also use Numpy and Math for evaluating formulas.

* Where will your test suite live?  Will you use `TravisCI`? `Coveralls`?
  - The test suite will receide in the Test sub-directory: both `TravisCI` and `Coveralls` will be used.
  
* How will you distribute your package (e.g. `PyPI`)?
  - We will distribute the package through `PyPI`

### Implementation
Discuss how you plan on implementing the forward mode of automatic differentiation.
* What are the core data structures?
  - We will be basing our formula parser on the above cited basic arithmetic formula parser. The code will create a formula data structure that will encode the user's input as an abstract syntax tree for ease of evaluation and differentiation.
* What classes will you implement?
  - The formula parser only supports basic arithmetic operations, so we will enrich the code with additional features: We will add support for parsing and evaluating variables and vectors. This will be a significant change from the current code as tese are new types of value tokens that need to be handled. We will also add unary operations for trigonometric functions and include pow(a,b) in the binary operations class.
* What method and name attributes will your classes have?
  - For the formula itself, we need to store the input text and the input variables.
  - For formula evaluation, we will need a parse method to first process the inputs. Then we will need another method that will take in a point for evaluation / differentiation. After these inputs are given, we can call eval or diff to get the value or derivative at the current, stored point.
* What external dependencies will you rely on?
  - As mentioned above, we will be using "https://ruslanspivak.com/lsbasi-part7/" as the basis for our parser code and evaluation code. We will also be using Math and Numpy to evaluate formulas and derivatives.
* How will you deal with elementary functions like `sin` and `exp`?
  - Basic trigonometric functions will be implemented as a unary operator in our abstract syntax tree. Their evaluation and differentiation will be coded in eval and diff using Numpy and or Math. Exp can be computed as pow(e, value). We will need to encode certain constants such as e and pi as protected names (ie. you can't have a variable called 'e' or 'pi')
  
### High Level Overview of Formulas:
* Abstract Syntax Tree Grammar
  - Value
    - VARIABLES (will need a class to store value and type ie. float or vector)
    - FLOATS
    - VECTOR (will need a vector class to overall __add__, __mult__, etc.)
  - BinOp
    - ADD
    - MINUS
    - MUL
    - DIV
    - POW
  - UnOp
    - SIN
    - COS
    - TAN
    - LOG
    
Note: Things enclosed in a parentheses will be parsed as a token. 

Be sure to consider a variety of use cases.  For example, don't limit your design to scalar
functions of scalar values.  Make sure you can handle the situations of vector functions of vectors and
scalar functions of vectors.  Don't forget that people will want to use your library in algorithms
like Newton's method (among others).

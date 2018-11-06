## How to install our package 
  - Our package can be found at https://pypi.org/project/AD-testing-packaging-CS207/:
  - Pip install your package from PyPI:
      - `pip install AD-testing-packaging-CS207`
  - Run the Python interpreter. 
      - `python`
  - And then import the module and it will tell you the installation was succesfull. 
      - `>>> import AD`

## Demo:
  - After importing AD type: 
      ```python
      >>> f1 = "POW(x, POW(x, x))";
      >>> vd = "x:2";
      >>> lexer = AD.interpreter.Lexer(f1);
      >>> parser =  AD.interpreter.Parser(lexer);
      >>> interpreter =  AD.interpreter.Interpreter(parser);
      >>> print('\nCalculating dif of {}, at {}'.format(f1, vd)) 
      >>> interpreter.diff_all(vd);
      d_x = 107.11041244660139
      ```
  - According to Wolfram Alfa this should give:
      32 (1 + 2 log^2(2) + log(4)) = 107.1104124466013909813974174582298585475873975011072538'

## How to install our package 
  - Our package can be found at https://pypi.org/project/AD-testing-packaging-CS207/:
  - Pip install your package from PyPI:
      - `pip install AD-testing-packaging-CS207`
  - Run the Python interpreter. 
      - `python`
  - And then import the module and it will tell you the installation was succesfull. 
      ```python 
      >>> import AD
      Installation Succes!
      Read the 'How-to-install and How-to-use.md' document for directions on how to use the package.
      ```

## How-to-use:
  - After importing AD in the Python interpreter you can use the automatic differentation package to evaluate the derivatiev of a function at a certain point in the following way:
    1. Define the function:
      ```python
      >>> f1 = "x*y*z" 
      ```
    2. Define the independant variables and their value where to calculate the derivative:
      ```python
      >>> vd = "x:2,y:3,z:4" 
      ```  
    3. Instatiate AD object:
      ```python
      >>> F1 = autodif.AD(f1) 
      ```  
    4. Evaluate and print all derivatives regarding to all independant variables:
      ```python      
      >>> F1.diff_all(vd)
      {'d_x': 12, 'd_y': 8, 'd_z': 6}
      ```      
    5. Evaluate the derivative regarding one specific independant variables:
      ```python      
      >>> F1.diff("x")
      12
      ```
    6. Evaluate the function at this specific point:
      ```python      
      >>> F1.val()
      24
      ```      
      
  - You can change the function we want to differentiate and the the point where we want to differentiate in the following way:      
      ```python      
      >>> F1.new_formula("a+b")
      >>> vd = "a:10, b : 1"
      >>> F1.set_point(vd)
      >>> print(F1.val())
      11
      >>> print(F1.diff_all())
      {'d_a': 1, 'd_b': 1} 
      >>> F1.diff("a")
      1
      ```
      
  - The following example results in a floating point derivative:
      ```python     
      >>> f="POW(x, POW(x, x))";
      >>> F1.new_formula(f)
      >>> vd = "x:2"
      >>> F1.set_point(vd)
      >>> print(F1.diff_all())
      {'d_x': 107.11041244660139}
      ```
      
  - The exact result of *Wolfram Alpha*:
       32 (1 + 2 log^2(2) + log(4)) 
       = __107.11041244660139__09813974174582298585475873975011072538'   
  - We obtain machine precision.
     

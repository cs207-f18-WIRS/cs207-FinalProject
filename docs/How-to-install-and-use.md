## How to install our package 
  - Our package can be found at https://pypi.org/project/AD-testing-packaging-CS207/:
  - Pip install your package from PyPI:
      - `pip install AD-testing-packaging-CS207`
  - Run the Python interpreter. 
      - `python`
  - And then import the module and it will tell you the installation was succesfull. 
      ```python 
      >>> import AD.autodif as autodif
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
  
![img](http://latex.codecogs.com/svg.latex?%5Cbegin%7Balign%7D%5Cdfrac%7Bd%7D%7Bdx%7D%5CBig%28f%28x%29%5CBig%29%26%3D%5Cdfrac%7Bd%7D%7Bdx%7D%5CBig%28x%5E%7Bx%5Ex%7D%5CBig%29%5Cnonumber%5C%5C%26%3Dx%5E%7Bx%5Ex%2Bx-1%7D%28x%5Clog%5E2%28x%29%2Bx%5Clog%28x%29%2B1%29%5Cnonumber%5C%5C%5Cend%7Balign%7D)

  - Evaluated at $x=2$ gives the following result:
  
![img](http://latex.codecogs.com/svg.latex?%%5Cbegin%7Balign%7D%5Cdfrac%7Bd%7D%7Bdx%7D%5CBig%28f%28x%3D2%29%5CBig%29%26%3D2%5E%7B2%5E2%2B2-1%7D%5Cbig%282%5Clog%5E2%282%29%2B2%5Clog%282%29%2B1%5Cbig%29%5Cnonumber%5C%5C%26%3D32%5Cbig%282%5Clog_2%282%29%2B2%5Clog%282%29%2B1%5Cbig%29%5Cnonumber%5C%5C%26%3D%5Cunderline%7B107.11041244660139%7D098139741...%5Cnonumber%5C%5C%5Cend%7Balign%7D)

  - We obtain machine precision.
    

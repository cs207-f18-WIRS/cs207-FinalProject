import pytest
import math
from AD import for_ad as f_ad

# Testing addition
a = f_ad.FD("a", 2, 1)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a+b+1)+2*c*d*3/(a*a)
print(str(e))
assert(e.grad() == -31)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 1)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a+b+1)+2*c*d*3/(a*a)
assert(e.grad() == -1)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 1)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a+b+1)+2*c*d*3/(a*a)
assert(e.grad() == 7.5)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 1)
e = 10-(1+a+b+1)+2*c*d*3/(a*a)
assert(e.grad() == 6)

# Testing subtraction
a = f_ad.FD("a", 2, 1)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a-b-1)+2*c*d*3/(a*a)
print(str(e))
assert(e.grad() == -31)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 1)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a-b-1)+2*c*d*3/(a*a)
assert(e.grad() == 1)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 1)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a-b-1)+2*c*d*3/(a*a)
assert(e.grad() == 7.5)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 1)
e = 10-(1+a-b-1)+2*c*d*3/(a*a)
assert(e.grad() == 6)

# Testing multiplication
a = f_ad.FD("a", 2, 1)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 0)
e = (10-(1+a+b+1)+2*c*d*3/(a*a)) ** (10-(1+a+b+1)+2*c*d*3/(a*a))
assert(abs(e.grad() + 1.799687241699159326140171557643555238493161738080837e52) < 1e45)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 1)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 0)
e = (10-(1+a+b+1)+2*c*d*3/(a*a)) ** (10-(1+a+b+1)+2*c*d*3/(a*a))
print(str(e))
assert(abs(e.grad() + 5.805442715158578471419908250463081414494070122841411e50) < 1e43)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 1)
d = f_ad.FD("d", 5, 0)
e = (10-(1+a+b+1)+2*c*d*3/(a*a)) ** (10-(1+a+b+1)+2*c*d*3/(a*a))
assert(abs(e.grad() - 4.3540820363689338535649311878473110608705525921310589e51) < 1e44)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 1)
e = 10-(1+a+b+1)+2*c*d*3/(a*a)
g = e**e
print(str(g))
assert(abs(g.grad() - 3.4832656290951470828519449502778488486964420737048471e51) < 1e44)

# Testing division
a = f_ad.FD("a", 2, 1)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a-b/1)+2*c/d*(3/a)
print(str(e))
assert(e.grad() == -2.2)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 1)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a-b/1)+2*c/d*(3/a)
assert(e.grad() == 1)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 1)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a-b/1)+2*c/d*(3/a)
assert(abs(e.grad() - 0.6) < 1e20)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 1)
e = 10-(1+a-b/1)+2*c/d*(3/a)
assert(e.grad() == -0.48)

# Testing power
a = f_ad.FD("a", 2, 1)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a**2*3**b+1)+2*c*d*3/(a*a)
print(str(e))
assert(e.grad() == -138)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 1)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a**2*3**b+1)+2*c*d*3/(a*a)
assert(abs(e.grad() - 118.650127176155846670686485587632776101928980244856940787) < 1e44)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 1)
d = f_ad.FD("d", 5, 0)
e = 10-(1+a**2*3**b+1)+2*c*d*3/(a*a)
assert(e.grad() == 7.5)

a = f_ad.FD("a", 2, 0)
b = f_ad.FD("b", 3, 0)
c = f_ad.FD("c", 4, 0)
d = f_ad.FD("d", 5, 1)
e = 10-(1+a**2*3**b+1)+2*c*d*3/(a*a)
assert(e.grad() == 6)

# Testing trig functions

# dx of sin(x) at x=0 : 1 (value 0)
a = f_ad.FD("a", 0, 1)
e = f_ad.FD.sin(a)
assert math.fabs(e.value - 0 ) < 1e-7
assert math.fabs(e.grad() - 1 ) < 1e-7
# dx of sin(x) at x=1 : 0.5403023058681397174009.. (value: 0.8414709848078965066525)
a = f_ad.FD("a", 1, 1)
e = f_ad.FD.sin(a)
assert math.fabs(e.value - 0.8414709848078965 ) < 1e-7
assert math.fabs(e.grad() - 0.5403023058681398 ) < 1e-7
# sin(0) and sin(1)
assert math.fabs(f_ad.FD.sin(0) - 0 ) < 1e-7
assert math.fabs(f_ad.FD.sin(1) - 0.8414709848078965 ) < 1e-7

# dx of cos(x) at x=0 : 1 (value 0)
a = f_ad.FD("a", 0, 1)
e = f_ad.FD.cos(a)
assert math.fabs(e.value - 1 ) < 1e-7
assert math.fabs(e.grad() - 0 ) < 1e-7
# dx of cos(x) at x=1 : 0.5403023058681397174009.. (value: -0.8414709848078965066525)
a = f_ad.FD("a", 1, 1)
e = f_ad.FD.cos(a)
assert math.fabs(e.value - 0.5403023058681398 ) < 1e-7
assert math.fabs(e.grad() + 0.8414709848078965 ) < 1e-7
# cos(0) and cos(1)
assert math.fabs(f_ad.FD.cos(0) - 1 ) < 1e-7
assert math.fabs(f_ad.FD.cos(1) - 0.5403023058681398 ) < 1e-7

# dx of tan(x) at x=0 : 0 (value A)
a = f_ad.FD("a", 0, 1)
e = f_ad.FD.tan(a)
assert math.fabs(e.value - 0 ) < 1e-7
assert math.fabs(e.grad() - 1 ) < 1e-7
# dx of tan(x) at x=1 : 3.425518820814759 760941.. (value: 1.557407724654902 2305..)
a = f_ad.FD("a", 1, 1)
e = f_ad.FD.tan(a)
assert math.fabs(e.value - 1.5574077246549023 ) < 1e-7
assert math.fabs(e.grad() - 3.425518820814759 ) < 1e-7
# tan(0) and tan(1)
assert math.fabs(f_ad.FD.tan(0) - 0 ) < 1e-7
assert math.fabs(f_ad.FD.tan(1) - 1.5574077246549023 ) < 1e-7

# dx of ln(x) at x=0 : 1/x => 1/0.5= 2.0
a = f_ad.FD("a", 0.5, 1)
e = f_ad.FD.ln(a)
assert math.fabs(e.value + 0.6931471805599453 ) < 1e-7
assert math.fabs(e.grad() - 2.0 ) < 1e-7
# ln(0.5)
assert math.fabs(f_ad.FD.ln(0.5) + 0.6931471805599453 ) < 1e-7

# dx of log(x, math.e) at x=0 : 1/x => 1/0.5= 2.0
a = f_ad.FD("a", 0.5, 1)
e = f_ad.FD.log(a,math.e)
assert math.fabs(e.value + 0.6931471805599453 ) < 1e-7
assert math.fabs(e.grad() - 2.0 ) < 1e-7
# ln(0.5)
assert math.fabs(f_ad.FD.log(0.5,math.e) + 0.6931471805599453 ) < 1e-7

# dx of arcsin(x) at x=0.5 = 1.1547005383792517 ( value : 0.5235987755982988 ) 
a = f_ad.FD("a", 0.5, 1)
e = f_ad.FD.arcsin(a)
assert math.fabs(e.value - 0.5235987755982988 ) < 1e-7
assert math.fabs(e.grad() - 1.1547005383792517 ) < 1e-7
# arcsin(0.5)
assert math.fabs(f_ad.FD.arcsin(0.5) - 0.5235987755982988 ) < 1e-7

# dx of arccos(x) at x=0.5 = - 1.1547005383792517 ( value : - 1.0471975511965976 ) 
a = f_ad.FD("a", 0.5, 1)
e = f_ad.FD.arccos(a)
assert math.fabs(e.value - 1.0471975511965976 ) < 1e-7
assert math.fabs(e.grad() + 1.1547005383792517 ) < 1e-7
# arcos(0.5)
assert math.fabs(f_ad.FD.arccos(0.5) - 1.0471975511965976 ) < 1e-7

# dx of arctan(x) at x=0.5 =  ( value :  ) 
a = f_ad.FD("a", 0.5, 1)
e = f_ad.FD.arctan(a)
assert math.fabs(e.value - 0.46364760900080615 ) < 1e-7
assert math.fabs(e.grad() - 0.8  ) < 1e-7
# arcos(0.5)
assert math.fabs(f_ad.FD.arctan(0.5) - 0.46364760900080615 ) < 1e-7

# dx of sinh(x)*cosh(x)**tanh(x)
a = f_ad.FD("a", 0.5, 1)
e = f_ad.FD.sinh(a)*f_ad.FD.cosh(a)*f_ad.FD.tanh(a)*f_ad.FD.sinh(2)*f_ad.FD.cosh(4)**f_ad.FD.tanh(6)
assert math.fabs(e.value - 26.89311502036146 ) < 1e-7
assert math.fabs(e.grad() - 116.39089610875486  ) < 1e-7

# dx of sqrt(x) at x=25 :  (value 25^0.5=5)
a = f_ad.FD("a", 25, 1)
e = f_ad.FD.sqrt(a)
assert math.fabs(e.value - 5 ) < 1e-7
assert math.fabs(e.grad() + 0.1 ) < 1e-7
assert math.fabs( f_ad.FD.sqrt(49) - 7 ) < 1e-7

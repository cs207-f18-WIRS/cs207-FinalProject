import pytest
import math
from AD import rev_ad as r_ad

# Testing addition
a = r_ad.Var("a", 2)
b = r_ad.Var("b", 3)
c = r_ad.Var("c", 4)
d = r_ad.Var("d", 5)
e = 10-(1+a+b+1)+2*c*d*3/(a*a)
e.grad_value = 1.0
print(str(e))
assert(a.grad() == -31)
assert(b.grad() == -1)
assert(c.grad() == 7.5)
assert(d.grad() == 6)

# Testing subtraction
a = r_ad.Var("a", 2)
b = r_ad.Var("b", 3)
c = r_ad.Var("c", 4)
d = r_ad.Var("d", 5)
e = 10-(1+a-b+1)+2*c*(d-3)/(a*a)
e.grad_value = 1.0
print(str(e))
assert(a.grad() == -5)
assert(b.grad() == 1)
assert(c.grad() == 1)
assert(d.grad() == 2)

# Testing multiplication
a = r_ad.Var("a", 2)
b = r_ad.Var("b", 3)
c = r_ad.Var("c", 4)
d = r_ad.Var("d", 5)
g = (10-(1+a+b+1)+2*c*d*3/(a*a))**(10-(1+a+b+1)+2*c*d*3/(a*a))
g.grad_value = 1.0
assert(abs(a.grad() + 1.799687241699159326140171557643555238493161738080837e52) < 1e45)
assert(abs(b.grad() + 5.805442715158578471419908250463081414494070122841411e50) < 1e43)
assert(abs(c.grad() - 4.3540820363689338535649311878473110608705525921310589e51) < 1e44)
assert(abs(d.grad() - 3.4832656290951470828519449502778488486964420737048471e51) < 1e44)

a = r_ad.Var("a", 2)
b = r_ad.Var("b", 3)
c = r_ad.Var("c", 4)
d = r_ad.Var("d", 5)
f = (10-(1+a+b+1)+2*c*d*3/(a*a))
g = f**f
g.grad_value = 1.0
print(str(g))
assert(abs(a.grad() + 1.799687241699159326140171557643555238493161738080837e52) < 1e-45)
assert(abs(b.grad() + 5.805442715158578471419908250463081414494070122841411e50) < 1e-43)
assert(abs(c.grad() - 4.3540820363689338535649311878473110608705525921310589e51) < 1e-44)
assert(abs(d.grad() - 3.4832656290951470828519449502778488486964420737048471e51) < 1e-44)

# Testing division
a = r_ad.Var("a", 2)
b = r_ad.Var("b", 3)
c = r_ad.Var("c", 4)
d = r_ad.Var("d", 5)
e = 10-(1+a-b/1)+2*c/d*(3/a)
e.grad_value = 1.0
print(str(e))
assert(a.grad() == -2.2)
assert(b.grad() == 1)
assert(abs(c.grad() - 0.6) < 1e-10)
assert(d.grad() == -0.48)

# Testing power
a = r_ad.Var("a", 2)
b = r_ad.Var("b", 3)
c = r_ad.Var("c", 4)
d = r_ad.Var("d", 5)
e = 10-(1+a**2*3**b+1)+2*c*d*3/(a*a)
e.grad_value = 1.0
print(str(e))
assert(a.grad() == -138)
assert(abs(b.grad() + 118.650127176155846670686485587632776101928980244856940787) < 1e-10)
assert(c.grad() == 7.5)
assert(d.grad() == 6)

# Testing trig functions
a = r_ad.Var("a", 2)
b = r_ad.Var("b", 3)
c = r_ad.Var("c", 4)
d = r_ad.Var("d", 5)
g = 10-(1+r_ad.sin(a)+r_ad.cos(b)+1)+2*r_ad.tan(c)*d*3/(a*a)
g.grad_value = 1.0
assert(abs(a.grad() + 8.26751278107468948653249990750416723363221998417802108488) < 1e-45)
assert(abs(b.grad() - 0.141120008059867222100744802808110279846933264252265584151) < 1e-43)
assert(abs(c.grad() - 17.55412591396215191291462436160988967759736172548402544260) < 1e-44)
assert(abs(d.grad() - 1.736731923524366374706013627400985884679644151050713195127) < 1e-44)

# Testing inverse trig functions
a = r_ad.Var("a", 0.2)
b = r_ad.Var("b", 0.3)
c = r_ad.Var("c", 0.4)
d = r_ad.Var("d", 5)
g = 10-(1+r_ad.arcsin(a)+r_ad.arccos(b)+1)+2*r_ad.arctan(c)*d*3/(a*a)
g.grad_value = 1.0
assert(abs(a.grad() + 2854.82) < 1e-2)
assert(abs(b.grad() - 1.04828) < 1e-2)
assert(abs(c.grad() - 6.46552) < 1e-2)
assert(abs(d.grad() - 0.57076) < 1e-2)

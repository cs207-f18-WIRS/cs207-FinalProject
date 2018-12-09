import pytest
import math
from AD import rev_ad as r_ad

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
assert(abs(a.grad() + 1.799687241699159326140171557643555238493161738080837e52) < 1e45)
assert(abs(b.grad() + 5.805442715158578471419908250463081414494070122841411e50) < 1e43)
assert(abs(c.grad() - 4.3540820363689338535649311878473110608705525921310589e51) < 1e44)
assert(abs(d.grad() - 3.4832656290951470828519449502778488486964420737048471e51) < 1e44)

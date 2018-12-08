import pytest
import math
from AD import for_ad as f_ad

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

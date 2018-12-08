import math
'''
Usage:
a = Var(3)
x = Var(2)
y = Var(3)
w = Var(4)
z = x*(x**y**w)/(y*w)

z.grad_value = 1.0

print(x.grad())
print(y.grad())
print(w.grad())
'''
class Var:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.grad_value = None

    def grad(self):
        if self.grad_value is None:
            self.grad_value = sum(val * var.grad() for val, var in self.children)
        return self.grad_value

    def __add__(self, other):
        if not isinstance(other, Var):
            z = Var(self.value + other)
            self.children.append((1.0, z))
            return z
        z = Var(self.value + other.value)
        other.children.append((1.0, z))
        self.children.append((1.0, z))
        return z

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Var):
            z = Var(self.value - other)
            self.children.append((1.0, z))
            return z
        z = Var(self.value - other.value)
        self.children.append((1.0, z))
        other.children.append((-1.0, z))
        return z

    def __rsub__(self, other):
        z = Var(other - self.value)
        self.children.append((-1.0, z))
        return z

    def __mul__(self, other):
        if not isinstance(other, Var):
            z = Var(self.value * other)
            self.children.append((other, z))
            return z
        z = Var(self.value * other.value)
        self.children.append((other.value, z))
        other.children.append((self.value, z))
        return z
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, Var):
            z = Var(self.value / other)
            self.children.append((1/other, z))
            return z
        z = Var(self.value / other.value)
        self.children.append((1/other.value, z))
        other.children.append((-self.value/other.value**2, z))
        return z

    def __rtruediv__(self, other):
        z = Var(other / self.value)
        self.children.append((-other/self.value**2, z))
        return z

    def __pow__(self, other):
        if not isinstance(other, Var):
            z = Var(self.value ** other)
            self.children.append((other*self.value**(other-1), z))
            return z
        z = Var(self.value ** other.value)
        self.children.append((other.value*self.value**(other.value-1), z))
        other.children.append((math.log(self.value)*self.value**other.value,z))
        return z

    def __rpow__(self, other):
        z = Var(other ** self.value)
        self.children.append((math.log(other)*other**self.value,z))
        return z

def sin(x):
    if not isinstance(x, Var):
        return math.sin(x)
    z = Var(math.sin(x.value))
    x.children.append((math.cos(x.value), z))
    return z


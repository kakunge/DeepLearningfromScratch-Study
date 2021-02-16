import numpy as np
from set import *

#재귀에서 반복문으로의 전환

A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)

#역전파
y.grad = np.array(1.0)
y.backward()
print(x.grad)#3.297442541400256
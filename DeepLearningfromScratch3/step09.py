import numpy as np
from set import *

def square(x):
    return Square()(x)

def exp(x):
    return Exp()(x)

x = Variable(np.array(0.5))
a = square(x)
b = exp(a)
y = square(b)
# y = square(exp(square(x)))

y.grad = np.array(1.0)
y.backward()

print(x.grad)#3.297442541400256

#Variable 오류 출력
p = Variable(np.array(1.0))
q = Variable(None)
r = Variable(1.0)#<class 'numpy.float64'>은(는) 지원하지 않습니다.

def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x
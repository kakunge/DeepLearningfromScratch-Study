import numpy as np
from dezero import Variable

def f(x):
    y = x **  4 - 2 * x ** 2

    return y

x = Variable(np.array(2.0))
iters = 10

y = f(x)
y.backward(create_graph=True)

print(x.grad)#variable(24.0)

gx = x.grad
x.cleargrad()
gx.backward()

print(x.grad)#variable(44.0)

for i in range(iters):
    print(i, x)

    y = f(x)
    x.cleargrad()
    y.backward(create_graph=True)

    gx = x.grad
    x.cleargrad()
    gx.backward()
    gx2 = x.grad

    x.data -= gx.data / gx2.data

#0 variable(2.0)
#1 variable(1.4545454545454546)
#2 variable(1.1510467893775467)
#3 variable(1.0253259289766978)
#4 variable(1.0009084519430513)
#5 variable(1.0000012353089454)
#6 variable(1.000000000002289)
#7 variable(1.0)
#8 variable(1.0)
#9 variable(1.0)
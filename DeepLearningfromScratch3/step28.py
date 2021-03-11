import numpy as np
from dezero import Variable
from dezero.core_simple import rosenbrock

x0 = Variable(np.array(0.0))
x1 = Variable(np.array(2.0))
y = rosenbrock(x0, x1)
y.backward()

print(x0.grad, x1.grad)#-2.0 400.0

x0.cleargrad()
x1.cleargrad()

lr = 0.001#learning rate
iters = 100000#iterations

for i in range(iters):
    print(x0, x1)

    y = rosenbrock(x0, x1)

    x0.cleargrad()
    x1.cleargrad()
    y.backward()

    x0.data -= lr * x0.grad
    x1.data -= lr * x1.grad

    #variable(0.999999999999928) variable(0.9999999999998557)
import numpy as np
import dezero.functions as F
from dezero import Variable

x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
y = F.sin(x)

print(y)
#variable([[ 0.84147098  0.90929743  0.14112001]
#          [-0.7568025  -0.95892427 -0.2794155 ]])

c = Variable(np.array([[10, 20, 30], [40, 50, 60]]))
d = x + c

print(d)
#variable([[11 22 33]
#          [44 55 66]])
'''
y.backward(retain_grad=True)

print(y.grad)
print(d.grad)
print(x.grad)
print(c.grad)
'''
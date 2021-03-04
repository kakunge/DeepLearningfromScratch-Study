from set import *

x = Variable(np.array(2.0))
y = -x

print(y)#variable(-2.0)

y1 = 2.0 - x
y2 = x - 1.0

print(y1)#variable(0.0)
print(y2)#variable(1.0)
from set import *

x = Variable(np.array(2.0))
a = square(x)
y = add(square(a), square(a))
y.backward()

print(y.data)#32.0
print(x.grad)#64.0
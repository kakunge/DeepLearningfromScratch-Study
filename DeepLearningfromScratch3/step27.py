import numpy as np
from dezero import Variable
from dezero.core_simple import sin, my_sin

x = Variable(np.array(np.pi/4))
y = sin(x)
y.backward()

print(y.data)#0.7071067811865475
print(x.grad)#0.7071067811865476

x.cleargrad()

z = my_sin(x)
z.backward()

print(z.data)#0.7071064695751781
print(x.grad)#0.7071032148228457

from dezero.utills import plot_dot_graph
x.name = 'x'
z.name = 'z'
plot_dot_graph(z, verbose=False, to_file='graphviz/img/my_sin.png')
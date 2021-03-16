import numpy as np
import matplotlib.pyplot as plt
from dezero import Variable
import dezero.functions as F

x = Variable(np.linspace(-7, 7, 200))
y = F.sin(x)
y.backward(create_graph=True)

logs = [y.data]

for i in range(3):
    gx = x.grad
    x.cleargrad()
    gx.backward(create_graph=True)

    print(x.grad)
#variable(-0.8414709848078965)
#variable(-0.5403023058681398)
#variable(0.8414709848078965)

labels = ['y=sin(x)', 'y`', 'y``', 'y```']
for i, v in enumerate(logs):
    plt.plot(x.data, logs[i], label=labels[i])
plt.legend(loc='lower right')
plt.show()
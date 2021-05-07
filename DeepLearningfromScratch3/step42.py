import numpy as np
from dezero import Variable
import dezero.functions as F

#토이 데이터셋 생성
np.random.seed(0)#시드값 고정
x = np.random.rand(100, 1)
y = 5 + 2 * x + np.random.rand(100, 1)#y에 무작위 노이즈 추가
x, y = Variable(x), Variable(y)

W = Variable(np.zeros((1, 1)))
b = Variable(np.zeros(1))
#y = Wx + b

def predict(x):
    y = F.matmul(x, W) + b

    return y

def mean_squared_error(x0, x1):
    diff = x0 - x1

    return F.sum(diff ** 2) / len(diff)

lr = 0.1
iters = 100

for i in range(iters):
    y_pred = predict(x)
    loss = mean_squared_error(y, y_pred)

    W.cleargrad()
    b.cleargrad()
    loss.backward()

    W.data = W.data - lr * W.grad.data
    b.data = b.data - lr * b.grad.data

    print(W, b, loss)

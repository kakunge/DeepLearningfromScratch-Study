import numpy as np
from functions import cross_entropy_error_batch, softmax

#계산 그래프 : 계산 과정을 그래프로 나타낸 것
#순전파 : 계산 그래프의 출발점부터 종착점으로의 전파
#역전파 : 순전파의 반대 방향으로 전파
#국소적 계산 : 자신과 관련된 작은 계산

#곱셈 계층
class mulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):#순전파
        self.x = x
        self.y = y
        out = x * y

        return out
    
    def backward(self, dout):#역전파
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy

#덧셈 계층
class addLayer:
    def __init__(self):
        pass

    def forward(self, x, y):#순전파
        out = x * y

        return out
    
    def backward(self, dout):#역전파
        dx = dout * 1
        dy = dout * 1

        return dx, dy

#ReLU 계층
class ReLU:
    def __init__(self):
        self.mask = None
    
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out
    
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx

#시그모이드 계층
class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        
        return out
    
    def backward(self, dout):
        dx = dout * (1.0 - self. out) * self.out
        
        return dx
    
#Affine 계층
class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b

        return out
    
    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        return dx

#Softmax-with-Loss 계층
class softmaxWithLoss:
    def __init__(self):
        self.loss = None#손실
        self.y = None#softmax 출력
        self.t = None#정답 레이블(원-핫 벡터)
    
    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error_batch(self.y, self.t)

        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx


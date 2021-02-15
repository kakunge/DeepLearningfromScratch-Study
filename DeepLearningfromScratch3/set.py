import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None#역전파에 대응하기 위한 미분값 저장

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        self.input = input#입력 변수를 기억
        
        return output

    def forward(self, x):
        raise NotImplementedError()

    def backward(self, gy):
        raise NotImplementedError()

class Square(Function):
    def forward(self, x):
        y = x ** 2

        return y

    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy

        return gx

class Exp(Function):
    def forward(self, x):
        y = np.exp(x)

        return y
    
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy

        return gx


#수치미분
def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)

    return (y1.data - y0.data) / (2 * eps)
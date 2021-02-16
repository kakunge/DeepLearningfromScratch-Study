import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None#역전파에 대응하기 위한 미분값 저장
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    #역전파 자동화
    '''
    def backward(self):
        f = self.creator#1. 함수를 가져온다
        if f is not None:
            x = f.input#2. 함수의 입력을 가져온다
            x.grad = f.backward(self.grad)#3. 함수의 backward 메서드를 호출한다
            x.backward()#하나 앞 변수의 backward 메서드를 호출한다
    '''

    #반복문을 이용한 구현
    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)
        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            x, y = f.input, f.output
            x.grad = f.backward(y.grad)

            if x.creator is not None:
                funcs.append(x.creator)

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        output.set_creator(self)#출력 변수에 창조자 설정
        self.input = input#입력 변수를 기억
        self.output = output#출력 저장
        
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
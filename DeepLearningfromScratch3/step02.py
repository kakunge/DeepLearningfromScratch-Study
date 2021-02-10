from step01 import Variable
import numpy as np

'''
class Function:
    def __call__(self, input):
        x = input.data
        y = x ** 2
        output = Variable(y)
        
        return output


x = Variable(np.array(10))
f = Function()
y = f(x)

print(type(y))#<class 'step01.Variable'>
print(y.data)#100
'''
#이후 모든 DeZero 함수는 Function 클래스 기반 클래스로서, 모든 함수에 공통되는 기능을 구현하며, 구체적인 함수는 Function 클래스를 상속한 클래스에서 구현한다.

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        
        return output

    def forward(self, x):
        raise NotImplementedError()

#Function 클래스를 상속하여 입력값을 제곱하는 클래스
class Square(Function):
    def forward(self, x):
        return x ** 2

x = Variable(np.array(10))
f = Square()
y = f(x)

print(type(y))#<class 'step01.Variable'>
print(y.data)#100

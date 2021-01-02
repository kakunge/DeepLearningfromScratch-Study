import numpy as np

def step_function1(x):#간단한 계단 함수
    if x > 0:
        return 1
    else:
        return 0
#넘파이 배열 사용 불가

def step_function2(x):#넘파이 배열 사용
    y = x > 0
    return y.astype(np.int)
#astype()은 넘파이 배열의 자료형을 바꿔준다

#시그모이드 함수 : 신경망에서 자주 쓰이는 활성화 함수의 하나
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#신경망에서 활성화 함수로 선형 함수를 사용하게 되면 신경망을 여러 층으로 구성하는 이점이 없기 때문에 활성화 함수는 반드시 비선형 함수를 이용해야 한다.
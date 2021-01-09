import numpy as np

#수치 미분 구현(중앙 차분 이용)
def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

#간단한 함수의 수치 미분
def function_1(x):
    return 2*x**2-3*x+4

print(numerical_diff(function_1, 5))#16.999999999995907
print(numerical_diff(function_1, 10))#36.99999999980719
#해석적인 결과와 거의 같게 나온다

def function_2(x):
    return x[0]**2 + x[1]**2

#편미분 : 해석적인 과정과 비슷하게 하나의 변수에 초점을 맞춰서 새로운 함수를 정의하여 수치 미분 함수를 적용한다.

#기울기
def numerical_gradient_1d(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]

        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val
    
    return grad

#다차원 배열 지원
def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 값 복원
        it.iternext()   
        
    return grad

#경사 하강법 - 최적화
def gradient_descent(f, init_x, lr=0.01, step_num=100):#f : 최적화 대상 함수, init_x : 초깃값, lr : learning rate(학습률), step_num : 경사법에 따른 반복 횟수
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x
#학습률이 너무 크면 발산하고, 너무 작으면 갱신이 잘 되지 않는다.

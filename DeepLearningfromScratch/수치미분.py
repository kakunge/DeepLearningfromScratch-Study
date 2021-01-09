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

#편미분 : 해석적인 과정과 비슷하게 하나의 변수에 초점을 맞춰서 새로운 함수를 정의하여 수치 미분 함수를 적용한다.

#기울기
def numerical_gradient(f, x):
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

#경사 하강법 - 최적화
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x


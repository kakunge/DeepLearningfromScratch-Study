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


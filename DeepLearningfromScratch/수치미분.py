import numpy as np

#수치 미분 구현(중앙 차분 이용)
def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)


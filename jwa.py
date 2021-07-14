import numpy as np
import random as ran

#좌표 설정
w, d, h = map(int, input().split())
arr = np.empty((w, d), int)

for i in range(w):
        for j in range(d):
            arr[i, j] = ran.randint(0, h)

rw, rd = ran.randint(0, w-2), ran.randint(0,d-2)
r = ran.randint(0, h)
arr[rw, rd] = arr[rw, rd+1] = arr[rw+1, rd] = arr[rw+1, rd+1] = r

print(rw, rd, r)
print(np.max(arr))
print(arr)

#드론 좌표 설정
dw = ran.randint(0, w)
dd = ran.randint(0, d)
dh = ran.randint(h+1, h+60)

print(dw, dd, dh)

#인식 가능 구역
ch = np.zeros((w, d))

#평면 거리 계산
distanceArr = np.zeros((w, d), float)
distance = 0

def dis(x, y):
    cx = (abs(dw-x)+0.5)**2
    cy = (abs(dd-y)+0.5)**2
    if x == dw:
        cx = 0.0
    if y == dd:
        cy = 0.0
    d = (cx+cy)
    return d

for i in range(w):
    for j in range(d):
        distance = dis(i, j)
        distanceArr[i, j] = distance
        if dw==i and dd==j:
            distanceArr[dw, dd] = 0.0

distanceArr = np.sqrt(distanceArr, distanceArr)

print(distanceArr)

#기울기 계산
slopeArr = np.zeros((w, d), float)
slope = 0
def slp(x, y):
    s = abs((dh-arr[x, y])/distanceArr[x, y])
    return s

for i in range(w):
    for j in range(d):
        slope = slp(i, j)
        slopeArr[i, j] = slope
        if dw==i and dd==j:
            slopeArr[dw, dd] = 0.0
        
print(slopeArr)

